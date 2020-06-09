import pyautogui as pg
import time


print('Module Started')
time.sleep(4) # Lag time between runnning and selecting where you want to type


def start():
    n = 1
    while n <= 100: # Total number of times executed
        time.sleep(18) # Dely (this will alleviate spamming)
        pg.hotkey('command', 'v')
        pg.hotkey('enter')
        n+=1
        print(str(n) + ' -- Out of 100') # Keeps track in terminal

start()



