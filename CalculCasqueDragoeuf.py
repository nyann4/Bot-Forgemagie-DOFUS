import re
from Macro1 import * 
from MainScreen import *
import random

def UpStats(list_value, nombre_item, tenta, tenta_plus, nombre_ligne_item):
    import json
    from pathlib import Path
    type_rune, indicatif = 0, 0
    under1_root_path = Path("..").resolve()
    path_dict_item = under1_root_path / "DictionnaireItem/item.json"
    with open(path_dict_item, encoding='utf-8') as outfile:
        data =json.load(outfile)
    A = int(list_value[0])
    B = int(list_value[1])
    C = int(list_value[2])
    D = int(list_value[3])
    E = int(list_value[4])
    F = int(list_value[5])
    print(A, B, C, D)
    nom_item = "Casque Dragoeuf"
    if not A > 134 :
        if (A > 89 and A <101) :
            type_rune, indicatif, done = selectRune(3, 1, data, nom_item)
        else :
            type_rune, indicatif, done = selectRune(2, 1, data, nom_item)
        return False, tenta,tenta_plus
    if not B > 7 :
        type_rune, indicatif, done = selectRune(1,2, data, nom_item)
        return False, tenta,tenta_plus
    if not C > 7 :
        type_rune, indicatif, done = selectRune(1,3, data, nom_item)
        return False, tenta,tenta_plus
    if not D > 7 :
        type_rune, indicatif, done = selectRune(1,4, data, nom_item)
        return False, tenta,tenta_plus
    if not E > 7 :
        type_rune, indicatif, done = selectRune(1,5, data, nom_item)
        return False, tenta,tenta_plus
    if not F > 7 :
        type_rune, indicatif, done = selectRune(1,6, data, nom_item)
        return False, tenta,tenta_plus
        #####
    if not B > 10 and A < 201:
        type_rune, indicatif, done = selectRune(1,2, data, nom_item)
        return False, tenta,tenta_plus
    if not C > 10 and A < 201:
        type_rune, indicatif, done = selectRune(1,3, data, nom_item)
        return False, tenta,tenta_plus
    if not D > 10 and A < 201:
        type_rune, indicatif, done = selectRune(1,4, data, nom_item)
        return False, tenta,tenta_plus
    if not E > 10 and A < 201:
        type_rune, indicatif, done = selectRune(1,5, data, nom_item)
        return False, tenta,tenta_plus
    if not F > 10 and A < 201:
        type_rune, indicatif, done = selectRune(1,6, data, nom_item)
        return False, tenta,tenta_plus
    if not (A > 190 and A < 201)  :
        if A < 201 :
            if (A ==0)or (A > 39 and A < 51) or (A > 89 and A < 101) or (A > 139 and A < 151):
                type_rune, indicatif, done = selectRune(3,1, data, nom_item) #Ra vi
            else :
                type_rune, indicatif, done = selectRune(2,1, data, nom_item) #Pa vi
        if A>200 :
            if A >200 and A < 206 :
                type_rune, indicatif, other_rune = selectRune5('ini')
            elif A > 205 :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        return False, tenta,tenta_plus
    if A > 190 and B > 10 and C > 10 and D >10 and E > 10 and F > 10 :
        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
        if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1  or list_1[1].find('Portée') != -1:
            OtherItem(nombre_item) 
        elif list_1[0].find('20 Initiative') != -1:
            if B < 13 :
                type_rune, indicatif, done = selectRune(1,2, data, nom_item)
            elif C < 13 :
                type_rune, indicatif, done = selectRune(1,3, data, nom_item)
            elif D < 13 :
                type_rune, indicatif, done = selectRune(1,4, data, nom_item)
            elif E < 13 :
                type_rune, indicatif, done = selectRune(1,5, data, nom_item)
            elif F < 13 :
                type_rune, indicatif, done = selectRune(1,6, data, nom_item)
            return False, tenta,tenta_plus
        else :
            type_rune, indicatif, other_rune = selectRune5('pa')
            time.sleep(0.3)
            tenta +=1    
        return False, tenta, tenta_plus