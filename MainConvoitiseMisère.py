from screen import screenValues
from CalculConvoitise import UpStats
from pynput.keyboard import Listener, Key
import signal
import os
from Macro1 import *
import time
from MainScreen import *
import pyautogui
from Reconnect import *

def on_release(key):
    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

def MainConvoitise():
    X = 0
    done = False
    while(done != True):
        time.sleep(0.35)
        list_value = screenValues(760, 341, 200, 37, 11)
        list_value = UpStats(list_value)
        X += 1
        print('Rune :' + str(X) )
        y = 200
        z = 100
        craming = 1500
        if X%z == 0 :
            # time.sleep(1.5)
            if X < 22500 :
                list_1 = screen(864, 477, 130, 33, 1)
                if 'Déconnexion\n\x0c' in list_1 :
                    ReconnectDofus(5, 10, 20, "convoitise de misere")
            else : 
                return True
        if X%y == 0 :
            Debug(900, 586)
            list_value = screenValues(760, 341, 200, 37, 11)
        if X%craming == 0 :
            time.sleep(0.5)
            Reset_stand('convoitise de misere')
            OtherF(1480, 210)
def Start():
    pyautogui.moveTo(1406, 133, duration=0.5)
    pyautogui.click(clicks=1) #clic sur la bonne catégorie d'item
    time.sleep(1)  
    start_fm(1339, 828 ,'convoitise de misere')
    OtherF(1480, 210) 

    with Listener(on_press=lambda k: None, on_release=on_release) as listener:
        MainConvoitise()
        listener.stop()