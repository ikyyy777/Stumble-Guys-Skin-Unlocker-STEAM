import os
import time
import webbrowser

def openDiscord():
    url = "https://discord.gg/UNdvHJBVxE"
    webbrowser.open(url)

try:
    print("Registering Name Changer Key...")
    os.startfile('Res\\Reg.bat')
    time.sleep(2)
    print("Registered, Now you can change your name for FREE!")
    os.system('pause')

    openDiscord()

except:
    print("Failed!")