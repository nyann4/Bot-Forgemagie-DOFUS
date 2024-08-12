from re import I
import time
import json
from screen import screenValues 

def UpStats2(list_value, poid, nombre_item,nombre_ligne_item, tenta, nom_item, mode, double_exo, carac_position):
    from Reconnect import calcul_poids_ligne, clean_string, suivis_value
    from Macro1 import selectRune, selectRune5, Scroll, OtherItem
    from MainScreen import screen
    from pathlib import Path
    import re
    from PIL import Image
    import pyautogui
    
    other_rune = False
    done = False
    tenta_plus = 0
    vita = int(list_value[0])
    force = int(list_value[1])
    sagesse = int(list_value[2])
    crit = int(list_value[3])
    pa = int(list_value[4])
    doneutre = int(list_value[5])
    doterre = int(list_value[6])
    reperfeu = int(list_value[8])
    tacle = int(list_value[9])
    retpm = int(list_value[10])
    docrit = int(list_value[11])
    other = False
    pui = calcul_poids_ligne(carac_position, list_value, nombre_ligne_item)
    under1_root_path = Path("..").resolve()
    path_dict_item = under1_root_path / "DictionnaireItem/item.json"

    with open(path_dict_item, encoding='utf-8') as outfile:
        data =json.load(outfile)
    near_perf = (vita > 389 and force > 77 and sagesse > 44 and crit == 6 and doneutre == 10 and doterre == 10 and reperfeu ==10 and tacle == 7 and retpm ==7 and docrit == 15)
    if mode == "overvita":
        min = 1
    if mode == "reperair":
        min = 6
    if mode == "dosort":
        min = 15

    max_poid = data[nom_item]['max_poid']

    list_carac = data[nom_item]['list_carac']
    for i in list_carac:
        if i == "Prospection" and int(list_value[6]) == 0:
            max_poid -= data['dict_poid_rune']['Prospection'] * data[nom_item]['Prospection']
    if (sum(pui) +170 +poid) < max_poid:
        type_rune, indicatif, other_rune = selectRune5('orbe')
        print('jet trop bas')
        return type_rune, indicatif, done, tenta, 0, other, other_rune

    if vita > 400 :
        if not near_perf:
            if vita < 406 :
                if force < 80:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
                else :
                    type_rune, indicatif, other_rune = selectRune5('ini')
            elif vita < 411:
                type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 416:
                if vita == 413:
                    type_rune, indicatif, other_rune = selectRune5('pod')
                else :
                    if sagesse < 50 :
                        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa
                    elif force < 78 :
                        type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaFo
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 421:
                if vita == 418 and force > 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
                else :
                    if tacle < 7:
                        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #Tacle
                    elif sagesse < 50 :
                        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa   
                    elif force < 78 :
                        type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaFo
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 426 :
                if vita == 423 and force > 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
                else :
                    if docrit < 15 :
                        type_rune, indicatif, done = selectRune(1,12, data, nom_item) #DoCrit
                    elif doneutre < 10 :
                        type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoNeutre
                    elif doterre < 10 :
                        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 431:
                if vita == 426:
                    type_rune, indicatif, other_rune = selectRune5('pod')   
                else :
                    if reperfeu < 10:                
                        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
                    else :
                        type_rune, indicatif, other_rune = selectRune5('ini')
            elif vita > 430 :
                if retpm < 7: 
                    type_rune, indicatif, done = selectRune(1,11, data, nom_item) #Retpm
                else :
                    type_rune, indicatif, other_rune = selectRune5('refeu')
            return type_rune, indicatif, done, tenta, poid, other, other_rune
    if force > 80 :
        if force == 81:
            if vita < 396 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vita
            else :
                type_rune, indicatif, other_rune = selectRune5('ini')
        if force == 82:
            type_rune, indicatif, other_rune = selectRune5('refeu')
        if force == 83:
            if sagesse < 50:
                type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa
            elif vita < 386:
                type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        if force == 84:
            if tacle < 7 :
                type_rune, indicatif, done = selectRune(1,10, data, nom_item) #Tacle
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        if force == 85:
            if doneutre < 10 :
                type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoNeutre
            elif doterre < 10 :
                type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
            elif docrit < 15 :
                type_rune, indicatif, done = selectRune(1,12, data, nom_item) #DoCrit
            else :
                type_rune, indicatif, other_rune = selectRune5('ini')
        if force == 86 :
            if reperfeu < 10 :
                type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
            else: 
                type_rune, indicatif, other_rune = selectRune5('ini')
        if force > 86 :
            if retpm < 7:
                type_rune, indicatif, done = selectRune(1,11, data, nom_item) #RetPm
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not pa == 1 and poid < min: 
        type_rune, indicatif, done = selectRune(1,5, data, nom_item) #PA
        exo_screen = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
        print('exo screen :', exo_screen)
        number = re.sub("[^0-9]","", exo_screen[0])
        exo_screen = clean_string(exo_screen)
        exo = str(number)+' '+ str(exo_screen[0])
        suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not sagesse > 35  : 
        print('not near perf')
        if sagesse == 0 or sagesse  == 10 or sagesse == 20 or sagesse == 30:
            type_rune, indicatif, done = selectRune(3,3, data, nom_item) #RaSa
        else :
            type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not crit > 4 :
        type_rune, indicatif, done = selectRune(1,4, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not docrit > 10 :
        type_rune, indicatif, done = selectRune(2,12, data, nom_item) #PaDoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not vita > 299 :
        if (vita>45 and vita<51) or (vita>95 and vita<101) or (vita>145 and vita<151) or (vita>195 and vita<201) or (vita>245 and vita<251) or (vita>295 and vita<300):
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        else :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not force >69:
        if force == 0 or force == 10 or force == 20 or force == 30 or force == 49 or force == 40 or force == 50 or force > 59 and force < 66 or force ==68 or force == 69 :
            type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaFo
        else :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaFo
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not retpm > 3 :
        type_rune, indicatif, done = selectRune(2,11, data, nom_item) #PaRetPm
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doneutre > 7:
        if doneutre == 7 :
            type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoNeutre
        else :
            type_rune, indicatif, done = selectRune(2,6, data, nom_item) #PaDoNeutre
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not tacle > 3 :
        type_rune, indicatif, done = selectRune(2,10, data, nom_item) #PaTac
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doterre > 7 :
        if doterre == 7 :
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
        else :
            type_rune, indicatif, done = selectRune(2,7, data, nom_item) #PaDoTerre
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not reperfeu > 7 :
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    ### FIN ETAPE 1 ###
    if not sagesse > 41 : 
        if sagesse == 40:
            type_rune, indicatif, done = selectRune(3,3, data, nom_item) #RaSa
        else :
            type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not crit > 5:
        type_rune, indicatif, done = selectRune(1,4, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not docrit > 12:
        if docrit == 12:
            type_rune, indicatif, done = selectRune(1,12, data, nom_item) #DoCrit
        else :
            type_rune, indicatif, done = selectRune(2,12, data, nom_item) #PaDoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not vita > 349:
        if  vita == 300 or (vita>339 and vita<351):
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        else :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not retpm > 5:
        type_rune, indicatif, done = selectRune(1,11, data, nom_item) #RetPm
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doneutre > 8:
        type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoNeutre
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not tacle > 5:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #Tac
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doterre > 8:
        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not reperfeu > 8:
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    ### FIN ETAPE 2 ###
    if not sagesse > 44 : 
        type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not crit > 5:
        type_rune, indicatif, done = selectRune(1,4, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not docrit > 13:
        type_rune, indicatif, done = selectRune(1,12, data, nom_item) #DoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not vita > 389:
        type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not force >77:
        type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaFo
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not retpm > 6:
        type_rune, indicatif, done = selectRune(1,11, data, nom_item) #RetPm
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doneutre > 9:
        type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoNeutre
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not tacle > 6:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #Tac
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doterre > 9:
        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoTerre
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not reperfeu > 9:
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not docrit > 14:
        type_rune, indicatif, done = selectRune(1,12, data, nom_item) #DoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if near_perf:
        if mode == "reperterre":
            if poid >= 51 and sagesse <48 and ( force > 78 or vita == 400) :
                type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 6
            if type_rune <= poid:
                type_rune, indicatif, other_rune = selectRune5('reperterre')
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
            print('exo :', list_value)
            if list_value[0].find('1% Résistance Terre') != -1 or list_value[0].find('2% Résistance Terre') != -1 or list_value[0].find('Fuite') != -1:
                if double_exo == 0 :
                    type_rune, indicatif, other_rune = selectRune5('po')
                    time.sleep(1)
                    Scroll('down')
                    list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                    Scroll('up')
                    if list_1[0].find('Po') != -1 or list_1[1].find('Po') != -1:
                        other = OtherItem(nombre_item)
                        if poid < 6:
                            poid = 0
                        other = 1
                    return type_rune, indicatif, done, tenta, poid, other, other_rune
                else :
                    if nombre_item > 1:
                        other = OtherItem(nombre_item)
                        type_rune, indicatif = 0, 7
                        return type_rune, indicatif, done, tenta, poid, other, other_rune
                    else :
                        type_rune, indicatif, done = 0, 7, True
                        return type_rune, indicatif, done, tenta, poid, other, other_rune
            else :
                other = OtherItem(nombre_item)
                if poid < 6:
                    poid = 0
                type_rune, indicatif = 0, 7
                return type_rune, indicatif, done, tenta, poid, other, other_rune

        if mode == "overvita" and poid > min:
            if poid >= 49 and sagesse <48 and force == 80 :
                type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 10
            if  type_rune <= poid  and vita < 456:
                type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 3
            if type_rune <= poid and vita < 491:
                type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 1
            if type_rune <= poid and vita < 501:
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vi
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            elif type_rune > poid or vita > 500:
                other = OtherItem(nombre_item)
                type_rune, indicatif, poid = 0, 7, 0
                return type_rune, indicatif, done, tenta, poid, other, other_rune

        elif mode == "overvita" and poid <= min :
            if vita < 450 :
                list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
                # if list_value[0].find('Po') == -1:
                #     type_rune, indicatif, other_rune = selectRune5('po')
                #     return type_rune, indicatif, done, tenta, poid, other, other_rune
                # else :
                other = OtherItem(nombre_item)
                type_rune, indicatif, poid = 0, 7, 0
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            else :
                other = OtherItem(nombre_item)
                type_rune, indicatif, poid = 0, 7, 0
                return type_rune, indicatif, done, tenta, poid, other, other_rune

        if mode == "dosort" :
            if poid >= 54 and sagesse <48 and force == 80 :
                type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 15 
            if type_rune <= poid :
                type_rune, indicatif, other_rune = selectRune5('dosort')
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
            if list_value[0].find('% Dommages aux sorts') != -1:
                other = OtherItem(nombre_item)
                type_rune, indicatif, poid = 0, 7, 0
            else :
                type_rune, indicatif, other_rune = selectRune5('po')
                indicatif = 7
            return type_rune, indicatif, done, tenta, poid, other, other_rune