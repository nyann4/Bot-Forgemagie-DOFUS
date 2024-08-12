import re
from weakref import KeyedRef
from Macro1 import * 
from MainScreen import *
import json

def UpStats(list_value, nombre_item, tenta, tenta_plus, nombre_ligne_item, type_exo, nom_item):
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
    path = "C:\\Users\\yannf\\OneDrive\\SWSetup\\Bureau\\PROJET0\\CODE\\all_codes\\DictionnaireItem\\item.json"
    with open(path, encoding='utf-8') as outfile:
        data =json.load(outfile)

    if not A > 19 :
        if A < 17 :
            type_rune, indicatif = selectRune(3,1, data, nom_item)
        else :
            type_rune, indicatif = selectRune(2,1, data, nom_item)
        return False, tenta, tenta_plus
    if not B > 3 :
        type_rune, indicatif = selectRune(1,2, data, nom_item)
        return False, tenta, tenta_plus
    if not D > 10 :
        type_rune, indicatif = selectRune(1,4, data, nom_item)
        return False, tenta, tenta_plus
    if not C > 1 :
        type_rune, indicatif = selectRune(2,3, data, nom_item)
        return False, tenta, tenta_plus
    if not A > 24 :
        type_rune, indicatif = selectRune(2,1, data, nom_item)
        return False, tenta, tenta_plus
    if not D > 11 :
        type_rune, indicatif = selectRune(1,4, data, nom_item)
        return False, tenta, tenta_plus
    if not B > 4 :
        type_rune, indicatif = selectRune(1,2, data, nom_item)
        return False, tenta, tenta_plus
    if not D > 12 :
        type_rune, indicatif = selectRune(1,4, data, nom_item)
        return False, tenta, tenta_plus
    if not A > 26 :
        type_rune, indicatif = selectRune(2,1, data, nom_item)
        return False, tenta, tenta_plus
    # if not C > 7 :
    #     if C == 6  :
    #         type_rune, indicatif = selectRune(2,3, data, nom_item)
    #     else : 
    #         type_rune, indicatif = selectRune(1,3, data, nom_item)
    #     return False, tenta, tenta_plus
    if not B > 5 and B < 7 :
        if B < 6 :
            type_rune, indicatif = selectRune(1,2, data, nom_item)
        if B > 6:
            type_rune, indicatif = selectRune(1,3, data, nom_item)
        return False, tenta, tenta_plus
    if not D > 13 :
        type_rune, indicatif = selectRune(1,4, data, nom_item)
        return False, tenta, tenta_plus
    if not C > 4 :
        if C < 4:
            type_rune, indicatif = selectRune(2,3, data, nom_item)
        else :
            type_rune, indicatif = selectRune(1,3, data, nom_item)
        return False, tenta, tenta_plus
    if A > 26 and B > 5 and C > 4 and D > 13 :
        list_1 = screen(750, (380+40*nombre_ligne_item), 200, 40, 2)
        if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1 or list_1[0].find('Portée') != -1  or list_1[1].find('Portée') != -1:
            OtherItem(nombre_item) 
        else :
            tenta+=1
            time.sleep(0.15)
            if type_exo == 1:
                type_rune, indicatif = selectRune5('pa')  
            elif type_exo == 2:
                type_rune, indicatif = selectRune5('pm')
            elif type_exo == 3:
                type_rune, indicatif = selectRune5('po')
            time.sleep(0.3)    
        return False, tenta, tenta_plus