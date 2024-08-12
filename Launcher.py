import pyautogui
from stopper import *
import os
import keyboard
import time
from pynput.keyboard import Listener, Key
import signal
import PIL.ImageGrab
from screen import screenValues
# from MainAnneauVolkorne import *
from MainConvoitiseMisère import *
# from MainAmuVolkorne import *

def on_release(key):
    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

def reset_raccourci_page():
    pyautogui.moveTo(1253, 989, duration=0.15) #reset page raccourci 
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.click(clicks=1, duration=0.05)
    pyautogui.moveTo(1253, 1031, duration=0.3)
    pyautogui.click(clicks=1) #met a la page 2 la page de raccourcis

def verify_quantity(x, y, Rune, quantity):
    pyautogui.moveTo(x, y, duration=0.5) #va dans la barre de recherche du coffre
    pyautogui.click(clicks=3) #triple clic pour tout selectionner et remplacer 
    time.sleep(0.5)
    pyautogui.write(Rune) #ecrit la rune 
    time.sleep(0.5)
    list_value = screenValues(1227, 210, 39, 17, 1) #screenshot la case de la rune
    manquant = quantity - int(list_value[0])
    print(manquant, Rune, "manquant") #ecrit la valeur lu
    return manquant

def takeRune(Rune, numberT, coefficient, Rab):
    quantity = ((int(numberT)*float(coefficient) ) + int(Rab))
    quantity = round(quantity) #defini la quantité a récupérer selon le nombre de tenta et le coefficient de runes par tenta
    manquant = verify_quantity(1373, 855, Rune, quantity)
    if manquant != 0 :
        pyautogui.moveTo(425, 852, duration=0.5) #va dans la barre de recherche du coffre
        pyautogui.click(clicks=3) #triple clic pour tout selectionner et remplacer 
        time.sleep(1)
        pyautogui.write(Rune) #ecrit la rune
        rgb = PIL.ImageGrab.grab().load()[326,211] #screen la couleur d'un pixel de cette case 
        # print(rgb, Rune)
        time.sleep(0.8)
        if rgb != (37, 44, 66):
            time.sleep(0.5)
            pyautogui.moveTo(339, 244, duration=0.5)
            pyautogui.dragTo(1273, 243 ,0.5,button='left') #amène toute les runes a l'inventaire
            time.sleep(0.5)
            pyautogui.write(str(manquant)) #ecrit la quantité a amener
            keyboard.press_and_release('enter')
        else : 
            print(manquant ,Rune , 'Manquants')
            
    verify_quantity(1373, 855, Rune, quantity)