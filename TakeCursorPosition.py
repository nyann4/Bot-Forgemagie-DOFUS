from pynput.keyboard import Listener, Key
import signal
import os
from Macro1 import *
import pyautogui
import keyboard

def takePosition():
    position1, position2  = pyautogui.position()
    return position1, position2

def on_release(key):

    if key == Key.tab:
        position1, position2 = takePosition()
        print(position1, position2)
        position  = (str(position1)+','+str(position2))
        with open('pos.txt', 'w') as filehandle:
            filehandle.write(position)
    if key == Key.space:  
        with open('pos.txt', 'r') as filehandle: #lis chaque ligne du .txt
            lines = filehandle.read()
        keyboard.press_and_release('backspace')
        keyboard.write(lines)

    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)
def position_get():
    with Listener(on_press=lambda k: None, on_release=on_release) as listener:

        listener.join()

position = position_get()
print(position)