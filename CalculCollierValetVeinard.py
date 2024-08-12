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
    other = False
    tenta_plus = 0
    vita = int(list_value[0])
    agilité = int(list_value[1])
    sagesse = int(list_value[2])
    pa = int(list_value[4])
    po = int(list_value[5])
    doair = int(list_value[6])
    reperfeu = int(list_value[8])
    repereau = int(list_value[9])
    esqpm = int(list_value[10])
    repou = int(list_value[11])
    
    pui = calcul_poids_ligne(carac_position, list_value, nombre_ligne_item)
    '''a remplacer par un get pixel si plus rapide pour detecter le message d'erreur'''
    under1_root_path = Path("..").resolve()
    path_dict_item = under1_root_path / "DictionnaireItem/item.json"

    with open(path_dict_item, encoding='utf-8') as outfile:
        data =json.load(outfile)
    near_perf = (vita > 340 and agilité > 77 and sagesse > 45 and doair == 20 and reperfeu ==10 and repereau == 7 and esqpm ==7 and repou == 20)
    if mode == "overvita":
        min = 1
    elif mode == "reperair":
        min = 6
    elif mode == "dosort":
        min = 15
    print('mode :', mode)

    list_carac = data[nom_item]['list_carac']
    if sum(pui) < 635 and poid < min and not near_perf and pa == 0:
        type_rune, indicatif, other_rune = selectRune5('orbe')
        print('jet trop bas')
        poid = 0
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if vita > 350 :
        if not near_perf:
            if vita < 356 :
                if agilité < 80:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Age
                else :
                    type_rune, indicatif, other_rune = selectRune5('ini')
            elif vita < 361:
                type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 366:
                if vita == 363:
                    type_rune, indicatif, other_rune = selectRune5('pod')
                else :
                    if sagesse < 50 :
                        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa
                    elif agilité < 78 :
                        type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaAge
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 371:
                if vita == 368 and agilité > 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
                else :
                    if sagesse < 50 :
                        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa   
                    elif agilité < 78 :
                        type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaAge
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 326 :
                if vita == 373 and agilité > 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Fo
                else :
                    if doair < 20 and doair != 17 :
                        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoAir
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 381:
                if vita == 376:
                    type_rune, indicatif, other_rune = selectRune5('pod')   
                else :
                    if reperfeu < 10:                
                        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
                    elif repereau < 7:
                        type_rune, indicatif, done = selectRune(1, 10, data, nom_item) #RePerEau
                    else :
                        type_rune, indicatif, other_rune = selectRune5('ini')
            elif vita > 380 :
                if esqpm < 7: 
                    type_rune, indicatif, done = selectRune(1,11, data, nom_item) #Retpm
                else :
                    type_rune, indicatif, other_rune = selectRune5('refeu')
            return type_rune, indicatif, done, tenta, poid, other, other_rune
    if agilité > 80 :
        if agilité == 81:
            if vita < 346 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vita
            else :
                type_rune, indicatif, other_rune = selectRune5('ini')
        if agilité == 82:
            if repou < 20 :
                type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePou
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        if agilité == 83:
            if sagesse < 50:
                type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa
            elif vita < 336:
                type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
            else :
                if repou < 20 :
                    type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePou
                else :
                    type_rune, indicatif, other_rune = selectRune5('refeu')
        if agilité == 84:
                if repou < 20 :
                    type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePou
                else :
                    type_rune, indicatif, other_rune = selectRune5('refeu')
        if agilité == 85:
            if doair < 20  and doair != 17:
                type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoAir
            else :
                type_rune, indicatif, other_rune = selectRune5('ini')
        if agilité == 86 :
            if reperfeu < 10 :
                type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
            elif repereau < 7:
                type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerEau
            else: 
                type_rune, indicatif, other_rune = selectRune5('ini')
        if agilité > 86 :
            if esqpm < 7:
                type_rune, indicatif, done = selectRune(1,11, data, nom_item) #RetPm
            else :
                if repou < 20 :
                    type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePou
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

    if not po == 1 and poid < min: 
        type_rune, indicatif, done = selectRune(1,6, data, nom_item) #Po
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not sagesse > 35  : 
        if sagesse == 0 or sagesse  == 10 or sagesse == 20 or sagesse == 30:
            type_rune, indicatif, done = selectRune(3,3, data, nom_item) #RaSa
        else :
            type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doair > 14 :
        type_rune, indicatif, done = selectRune(2,7, data, nom_item) #PaDoAir
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not vita > 299 :
        if (vita>45 and vita<51) or (vita>95 and vita<101) or (vita>145 and vita<151) or (vita>195 and vita<201) or (vita>245 and vita<251) or (vita>290 and vita<306):
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        else :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not agilité >69:
        if agilité == 0 or agilité == 10 or agilité == 20 or agilité == 30 or agilité == 49 or agilité == 40 or agilité == 50 or agilité > 59 and agilité < 66 or agilité ==68 or agilité == 69 :
            type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaAge
        else :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaAge
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not esqpm > 3 :
        type_rune, indicatif, done = selectRune(2,11, data, nom_item) #PaEsqPm
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not repereau > 4:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerEau
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not repou > 14 :
        type_rune, indicatif, done = selectRune(2,12, data, nom_item) #PaRePou
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

    if not doair > 16:
        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoAir
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    
    if not esqpm > 5:
        type_rune, indicatif, done = selectRune(1,11, data, nom_item) #EsqPm
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not repereau > 5:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerEau
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not repou > 16:
        type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePou
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not reperfeu > 8:
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    ### FIN ETAPE 2 ###
    if not sagesse > 45 : 
        type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not agilité >77:
        type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaAge
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not esqpm > 6:
        type_rune, indicatif, done = selectRune(1,11, data, nom_item) #EsqPm
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not repou > 19:
        if repou == 17 :
            type_rune, indicatif, done = selectRune(2,12, data, nom_item) #PaRePou
        else :
            type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePou
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not vita > 340:
        if  vita < 327 or vita>335:
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        else :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not repereau > 6:
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerEau
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if not reperfeu > 9:
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not doair > 19:
        if doair == 17 :
            type_rune, indicatif, done = selectRune(2,7, data, nom_item) #PaDoAir
        else :
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoAir
        return type_rune, indicatif, done, tenta, poid, other, other_rune
    
    if near_perf and poid >= min:
        if mode == "reperair":
            if poid >= 51 and sagesse <48 and ( agilité > 78 or vita == 400) :
                type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 6
            if type_rune <= poid:
                type_rune, indicatif, other_rune = selectRune5('reperair')
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
            print('exo :', list_value)
            if list_value[0].find('1% Résistance') != -1 or list_value[0].find('2% Résistance') != -1 :
                if double_exo == 1 :
                    type_rune, indicatif, other_rune = selectRune5('dosort')
                    time.sleep(1.5)
                    Scroll('down')
                    list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                    Scroll('up')
                    if list_1[0].find('Résistance') != -1 or list_1[1].find('Résistance') != -1:
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
            if poid >= 49 and sagesse <48 and agilité == 80 :
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
            elif type_rune > poid or vita > 440:
                other = OtherItem(nombre_item)
                type_rune, indicatif, poid = 0, 7, 0
                return type_rune, indicatif, done, tenta, poid, other, other_rune

        elif mode == "overvita" and poid <= min :
            if vita < 390 :
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
            if vita < 349  and poid%min >= 3:
                type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            if vita < 346 and poid%min >= 1:
                type_rune, indicatif, done = selectRune(1,1, data, nom_item) #PaVi
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            # if poid >= 54 and sagesse <48 and agilité == 80 :
            #     type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaSa
            #     return type_rune, indicatif, done, tenta, poid, other, other_rune
            type_rune = 15 
            if type_rune <= poid :
                type_rune, indicatif, other_rune = selectRune5('dosort')
                return type_rune, indicatif, done, tenta, poid, other, other_rune
            list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
            if list_value[0].find('% Dommages aux sorts') != -1:
                other = OtherItem(nombre_item)
                type_rune, indicatif, poid = 0, 7, 0
            else :
                type_rune, indicatif, other_rune = selectRune5('pm')
                indicatif = 7
            return type_rune, indicatif, done, tenta, poid, other, other_rune
    if near_perf and poid < min :
        list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
        if list_value[0].find('% Dommages aux sorts') != -1:
            other = OtherItem(nombre_item)
            type_rune, indicatif, poid = 0, 7, 0
        else :
            type_rune, indicatif, other_rune = selectRune5('dosort')
        return type_rune, indicatif, done, tenta, poid, other, other_rune