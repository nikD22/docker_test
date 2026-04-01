import time
import requests
import colorama
from colorama import Fore

colorama.init()

while True:
    print(Fore.GREEN + "hello" + Fore.RESET, flush=True)
    time.sleep(1)
