import re
from Macro1 import * 
from MainScreen import *
import random

def UpStats(list_value, nombre_item, tenta, tenta_plus, nombre_ligne_item, type_exo):
    try :
        A = int(list_value[0])
        B = int(list_value[1])
        C = int(list_value[2])
        D = int(list_value[3])
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return False, tenta, tenta_plus
    print(A, B, C, D)

    if not A > 19 :  
        if A < 17 :
            selectRune(3, 1)
        else :
            selectRune(2, 1)
        return False, tenta, tenta_plus
    if not B > 3 : # Critique
        selectRune(1, 2)
        return False, tenta, tenta_plus
    if not D > 10 :
        selectRune(1, 4)
        return False, tenta, tenta_plus
    if not C > 5 : # Do crit
        selectRune(2, 3)
        return False, tenta, tenta_plus
    if not A > 24 : #Puissance
        selectRune(2, 1)
        return False, tenta, tenta_plus
    if not D > 11 : # Do mélée
        selectRune(1, 4)
        return False, tenta, tenta_plus
    if not B > 4 :  #Critique
        selectRune(1, 2)
        return False, tenta, tenta_plus
    if not D > 12 : #Do mélée
        selectRune(1, 4)
        return False, tenta, tenta_plus
    if not B > 5 and B < 7 : #Critique
        if B < 6 :
            selectRune(1, 2)
        if B > 6:
            selectRune(1, 3)
        return False, tenta, tenta_plus
    if not D > 14 : # Do mélée
        selectRune(1, 4)
        return False, tenta, tenta_plus
    if not C > 8 : # Do crit
        if C == 6 or C == 7:
            selectRune(2, 3)
        else : 
            selectRune(1, 3)
        return False, tenta, tenta_plus
    if A > 24 and B > 5 and C > 8 and D == 15 :
        list_1 = screen(750, (380+40*nombre_ligne_item), 200, 40, 2)
        if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1 or list_1[0].find('Portée') != -1  or list_1[1].find('Portée') != -1:
            OtherItem(nombre_item) 
        else :
            tenta+=1
            time.sleep(0.15)
            if type_exo == 1:
                selectRune5(811, 1030)  
            elif type_exo == 2:
                selectRune5(1164, 1030)
            elif type_exo == 3:
                selectRune5(1124, 990)
            time.sleep(0.3)
            CleanRune()   #Ga PM      
        return False, tenta, tenta_plus
