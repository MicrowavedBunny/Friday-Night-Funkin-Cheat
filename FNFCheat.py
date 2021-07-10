#This was created using Python 3.9 but can cause issue with the dependicies supposedly using Python 3.7 will mitigate this 
#You have to play in full screen on 1080p display or get you own values retard
#Same goes for keybinds
#You are a big boy figure it out
#x: 1108 y: 958 (181, 213, 218) = left arrow - keybind is Z
#x: 1266 y: 956 (194, 226, 229) = down arrow - keybind is X
#x: 1425 y: 956 (168, 200, 208) = up arrow - keybind is .
#x: 1579 y: 958 (181, 212, 218) = right arrow - keybind is /
from pyautogui import *
import pyautogui
import keyboard



while keyboard.is_pressed('q') == False:
    if keyboard.is_pressed('h') == True:
        while keyboard.is_pressed('q') == False:

            zpixel = pyautogui.pixelMatchesColor(1108, 958, (181, 213, 218), tolerance=10)
            xpixel = pyautogui.pixelMatchesColor(1266, 956, (194, 226, 229), tolerance=10)
            dotpixel = pyautogui.pixelMatchesColor(1425, 956, (168, 200, 208), tolerance=10)
            slashpixel = pyautogui.pixelMatchesColor(1579, 958, (181, 212, 218), tolerance=10)

            if zpixel == False:
                keyboard.press('Z')
                keyboard.release('Z')
                print('z')
            if  xpixel == False:
                keyboard.press('x')
                keyboard.release('x')
                print('x')
            if dotpixel == False:
                keyboard.press('.')
                keyboard.release('.')
                print('.')
            if slashpixel == False:
                keyboard.press('/')
                keyboard.release('/')
                print('/')
