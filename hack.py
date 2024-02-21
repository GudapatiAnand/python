import pyautogui as pt
import time

limit = input("enter the limit :")
msg = input("Enter the Msg :")
i=1

time.sleep(6)

while i <= int(limit):

    pt.typewrite(msg)
    pt.press("enter")

    i +=1
