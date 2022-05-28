import os
import time
import shutil
import colorama
import webbrowser

from colorama import Fore
colorama.init()

def openDiscord():
    url = "https://discord.gg/UNdvHJBVxE"

    webbrowser.open(url)

def main():
    while True:
        print(Fore.BLUE+"Stumble Guys Unlocker | Made by 1ntrovertskrrt\n"+Fore.WHITE)
        print("Enter Stumble Guys Directory!")
        print("Example D:\SteamLibrary\steamapps\common\Stumble Guys")

        try:
            dll_location = "Res\\Assembly-CSharp.dll"
            input_game_location = str(input(">> "))
            game_location = input_game_location+"\Stumble Guys_Data\Managed"
            print(Fore.CYAN+"Injecting...\n")
            time.sleep(2)
            shutil.copy(dll_location,game_location)
            print(Fore.GREEN+"Injected!")
            time.sleep(2)
            openDiscord()
            break

        except:
            print(Fore.RED+"Game Not Found!"+Fore.WHITE)
            os.system('pause')
            os.system('cls')
            main()
    
main()