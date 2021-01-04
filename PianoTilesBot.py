from pyautogui import *
import pyautogui 
import time
import keyboard
import random
import win32api, win32con

## This code is written to win on https://poki.com/en/g/piano-tiles-2 , it was written in an hour cuz I was bored, yes the numbers below are manually aquired (wont work on different screens)
## Tile 1: 715
##Tile 2: 810
## Tile 3: 923
##Tile 4: 1020
## Y for all: 650
## Start button value 54 159 198
## Hold: 0 2 33



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

GameStarted = False

try:
    while keyboard.is_pressed('q') == False:
        if GameStarted == False:
            if pyautogui.pixel(715,650)[0] == 54 and pyautogui.pixel(715,650)[1] == 159 and pyautogui.pixel(715,650)[2] == 198:
                click(715,650)
                GameStarted=True
                print(GameStarted)
            if pyautogui.pixel(810,650)[0] == 54 and pyautogui.pixel(810,650)[1] == 159 and pyautogui.pixel(810,650)[2] == 198:
                click(810,650)
                GameStarted=True
                print(GameStarted)
            if pyautogui.pixel(923,650)[0] == 54 and pyautogui.pixel(923,650)[1] == 159 and pyautogui.pixel(923,650)[2] == 198:
                click(923,650)
                GameStarted=True
                print(GameStarted)
            if pyautogui.pixel(1020,650)[0] == 54 and pyautogui.pixel(1020,650)[1] == 159 and pyautogui.pixel(1020,650)[2] == 198:
                click(1020,650)
                GameStarted=True
                print(GameStarted)
        
        if pyautogui.pixel(715,650)[1] == 1 or pyautogui.pixel(715,650)[1] == 2 :
            click(715,650)
            time.sleep(0.01)
        if pyautogui.pixel(810,650)[1] == 1 or pyautogui.pixel(810,650)[1] == 2:
            click(810,650)
            time.sleep(0.01)
        if pyautogui.pixel(923,650)[1] == 1 or pyautogui.pixel(923,650)[1] == 2:
            click(923,650)
            time.sleep(0.01)
        if pyautogui.pixel(1020,650)[1] == 1 or pyautogui.pixel(1020,650)[1] == 2:
            click(1020,650)
            time.sleep(0.01)
        
except :
    pass 