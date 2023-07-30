import sys
import time
import requests
from colorama import Fore, init
import os
import asyncio

init()

def check_webhook(webhook):
    try:
        with requests.get(webhook) as r:
            return r.status_code == 200
    except:
        return False


def inflate_message(message):
    message = f"@everyone - {message}\n"
    message = message * (999 // len(message) + 1)
    return message


def spam_webhook(webhook, message):
    r = requests.post(webhook, json={"content": message})
    return r.status_code


def spam_threads(webhook, message, iterations):
    for x in range(iterations):
        for y in range(5):
            status_code = spam_webhook(webhook, message)
            if status_code == 204:
                print(f"{Fore.GREEN}Status: OK{Fore.RESET}")
            elif status_code == 429:
                print(f"{Fore.RED}Oops! Rate Limited.. Trying again in 5 seconds...{Fore.RESET}")
                time.sleep(5)
            else:
                print(f"{Fore.YELLOW}{status_code}{Fore.RESET}")
                str(input(f"{Fore.YELLOW}Press anything to exit..."))
                sys.exit()


class WebhookSpam:
    def __init__(self):
        print("Made with some love from New Zealand\n")
        self.choice = int(input(f"{Fore.YELLOW}To continue, press 9 {Fore.RESET}>>> "))

        if self.choice not in [9]:
            print(f"{Fore.RED}Invalid Choice! Exiting...\n")
            time.sleep(2)
            sys.exit()

        if self.choice == 9:
            self.webhook = str(input(f"{Fore.YELLOW}Enter Discord Webhook Address {Fore.RESET}>>> "))

            if not check_webhook(self.webhook):
                print(f"{Fore.RED}The Supplied Webhook is no longer valid!{Fore.RESET}")
                time.sleep(2)
                sys.exit()

            self.message = str(input(f"{Fore.YELLOW}Enter Your Message: {Fore.RESET}>>> "))
            self.iterations = int(input(f"{Fore.YELLOW}Enter Number of Iterations: {Fore.RESET}>>> "))
            if self.iterations < 0:
                print(f"{Fore.RED}Invalid Input{Fore.RESET}")
                time.sleep(2)
                sys.exit()

            spam_threads(self.webhook, inflate_message(self.message), self.iterations)


if __name__ == "__main__":
    # Clear the terminal screen on Windows or exit on non-Windows systems
    if os.name == "nt":
        os.system("cls")
