from re import I
import time
import json
from screen import screenValues 

def UpStats2(list_value, poid, nombre_item, nombre_ligne_item, tenta, nom_item, carac_position):
    from Reconnect import calcul_poids_ligne, clean_string, suivis_value
    from Macro1 import selectRune, selectRune5, Scroll, OtherItem
    from MainScreen import screen
    from pathlib import Path
    import re
    from PIL import Image
    import pyautogui

    done = False
    tenta_plus = 0
    vita = int(list_value[0])
    force = int(list_value[1])
    intelligence = int(list_value[2])
    agilité = int(list_value[3])
    crit = int(list_value[4])
    pa = int(list_value[5])
    doterre = int(list_value[6])
    dofeu = int(list_value[7])
    doair = int(list_value[8])
    soins = int(list_value[9])
    other = False
    pui = calcul_poids_ligne(carac_position, list_value, nombre_ligne_item)
    '''a remplacer par un get pixel si plus rapide pour detecter le message d'erreur'''
    list_error = screenValues(853, 487, 200, 40, 1 )
    if list_error[0].find('Erreur') != -1  or list_error[0].find('Attention') != -1 or list_error[0].find('Information') != -1:
        time.sleep(0.5)
        pyautogui.click(919,582)
        type_rune, indicatif = 0, 8
        return type_rune, indicatif, done, tenta, poid, other
    under1_root_path = Path("..").resolve()
    path_dict_item = under1_root_path / "DictionnaireItem/item.json"

    with open(path_dict_item, encoding='utf-8') as outfile:
        data =json.load(outfile)
    max_poid = data[nom_item]['max_poid']

    near_perf = (vita > 124 and force == 40 and intelligence == 40 and agilité == 40 and crit> 2 and doterre == 2 and dofeu == 2 and doair == 2 )

    if vita > 130 :
        # if not near_perf:
            if vita < 141 :
                if not force >  39:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
                elif not intelligence >  39:
                    type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Intel
                elif not agilité >  39:
                    type_rune, indicatif, done = selectRune(1,4, data, nom_item) #Agi
                else :
                    type_rune, indicatif,other_rune = selectRune5('ini')
            elif vita > 140 :
                if not force >  37:
                    type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaFo
                elif not intelligence >  37:
                    type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaIntel
                elif not agilité >  37:
                    type_rune, indicatif, done = selectRune(2,4, data, nom_item) #PaAgi
                else :
                    type_rune, indicatif,other_rune = selectRune5('refeu')
            return type_rune, indicatif, done, tenta, poid, other
    min = 10

    if not pa == 1 and (poid < min or crit == 5):
        type_rune, indicatif, done = selectRune(1,6, data, nom_item) #PA
        exo = 0
        suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
        return type_rune, indicatif, done, tenta, poid, other  

    if not soins > 2 and pa == 1 and crit < 4:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #Soins
        return type_rune, indicatif, done, tenta, poid, other

    if not vita >99  and intelligence < 41 and force < 41 and agilité < 41:
        if vita < 81 :
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        else :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other

    if not crit > 1 and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,5, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other

    if not force > 33  and intelligence < 41 and agilité < 41:
        if force < 31 :
            type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaFo
        else :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaFo
        return type_rune, indicatif, done, tenta, poid, other

    if not doterre > 0 and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
        return type_rune, indicatif, done, tenta, poid, other

    if not intelligence > 33  and force < 41 and agilité < 41:
        if intelligence < 31 :
            type_rune, indicatif, done = selectRune(3,3, data, nom_item) #RaIne
        else :
            type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaIne
        return type_rune, indicatif, done, tenta, poid, other

    if not dofeu > 0  and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,8, data, nom_item) #DoFeu
        return type_rune, indicatif, done, tenta, poid, other

    if not agilité > 33  and intelligence < 41 and force < 41 :
        if agilité < 31 :
            type_rune, indicatif, done = selectRune(3,4, data, nom_item) #RaAge
        else :
            type_rune, indicatif, done = selectRune(2,4, data, nom_item) #PaAge
        return type_rune, indicatif, done, tenta, poid, other

    if not doair > 0  and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #DoAir
        return type_rune, indicatif, done, tenta, poid, other

    if not crit > 2  and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,5, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other

    if not vita > 114  and intelligence < 41 and force < 41 and agilité < 41:
        if vita < 120:
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        else :
            type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vi
        return type_rune, indicatif, done, tenta, poid, other

    if not force == 40  and intelligence < 41  and agilité < 41:
        if force < 40 :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaFo
        if force >40 :
            if intelligence < 40 :
                type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Ine
            elif agilité < 40 :
                type_rune, indicatif, done = selectRune(1,4, data, nom_item) #Age
            elif vita < 126 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vita
            else :
                type_rune, indicatif,other_rune = selectRune5('ini')
        return type_rune, indicatif, done, tenta, poid, other

    if not doterre > 1 and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
        return type_rune, indicatif, done, tenta, poid, other

    if not intelligence == 40  and force < 41 and agilité < 41:
        if intelligence < 40 :
            type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaIne
        if intelligence >40 :
            if force < 40 :
                type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
            elif agilité < 40 :
                type_rune, indicatif, done = selectRune(1,4, data, nom_item) #Age
            elif vita < 126 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vita
            else :
                type_rune, indicatif,other_rune = selectRune5('ini')
        return type_rune, indicatif, done, tenta, poid, other

    if not dofeu > 1 and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,8, data, nom_item) #DoFeu
        return type_rune, indicatif, done, tenta, poid, other

    if not agilité == 40  and intelligence < 41 and force < 41 :
        if agilité < 40 :
            type_rune, indicatif, done = selectRune(2,4, data, nom_item) #PaAge
        if agilité >40 :
            if force < 40 :
                type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Ine
            elif intelligence < 40 :
                type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Ine
            elif vita < 126 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vita
            else :
                type_rune, indicatif,other_rune = selectRune5('ini')
        return type_rune, indicatif, done, tenta, poid, other
    
    if not doair > 1 and intelligence < 41 and force < 41 and agilité < 41:
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #DoAir
        return type_rune, indicatif, done, tenta, poid, other

    if not vita > 124  and intelligence < 41 and force < 41 and agilité < 41:
        if vita >119:
            type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vi
        else :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other

    if not soins > 4 and pa == 1 and crit < 4:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #Soins
        return type_rune, indicatif, done, tenta, poid, other

    if near_perf :
        type_rune = 10 
        if type_rune <= poid and crit < 5:
            type_rune, indicatif, done = selectRune(1,5, data, nom_item) #Crit
            return type_rune, indicatif, done, tenta, poid, other
        else:
            if crit > 4 :
                type_rune, indicatif = 0, 0
                OtherItem(nombre_item)
                return type_rune, indicatif, done, tenta, poid, True
            else :
                list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
                if list_value[0].find('(dommages Terre)') != -1:
                    type_rune, indicatif,other_rune = selectRune5('po')
                    time.sleep(1.25)
                    return type_rune, indicatif, done, tenta, poid, other
                else :
                    type_rune, indicatif = 0, 0
                    OtherItem(nombre_item)
                    return type_rune, indicatif, done, tenta, poid, True