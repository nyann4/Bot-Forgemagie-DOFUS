import time
from MainScreen import *
import re
from Macro1 import * 

def UpStats2(list_value, poid, nombre_item, nombre_ligne_item, tenta, nom_item, mode, double_exo, carac_position):
    from screen import screenValues
    from pathlib import Path
    import json
    other_rune = False
    other, done = False, False
    vita = int(list_value[0])
    intelligence = int(list_value[1])
    sagesse = int(list_value[2])
    crit = int(list_value[3])
    pa = int(list_value[4])
    invo = int(list_value[5])
    dofeu = int(list_value[6])
    prospe = int(list_value[7])
    reperfeu = int(list_value[8])
    esqpm = int(list_value[9])
    docrit = int(list_value[10])
    under1_root_path = Path("..").resolve()
    path_dict_item = under1_root_path / "DictionnaireItem/item.json"
    with open(path_dict_item, encoding='utf-8') as outfile:
        data =json.load(outfile)

    if mode == "reperfeu" :
        min = 6
    if mode == "overvita" :
        min = 1
    if mode == "dosort":
        min = 15

    near_perf = (vita > 389 and intelligence > 94 and sagesse > 37 and crit > 4 and dofeu > 19 and reperfeu > 9 and esqpm > 9 and docrit > 14)

    if vita > 400 :
        if not near_perf or mode != "overvita":
            if vita < 406 :
                if intelligence < 100:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Ine
                else :
                    type_rune, indicatif, other_rune = selectRune5('ini')
            elif vita < 411:
                if vita == 406 :
                    type_rune, indicatif, other_rune = selectRune5('ini')
                else :
                    type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 416:
                if vita == 413 or vita == 412:
                    type_rune, indicatif, other_rune = selectRune5('pod')
                elif vita == 414 or vita == 415 :
                    if sagesse < 40 :
                        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa
                    elif intelligence < 78 :
                        type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaIne
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
                else :
                    type_rune, indicatif, other_rune = selectRune5('ini')
            elif vita < 421:
                if (vita == 418 or vita ==417) and intelligence > 60 and intelligence < 100:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Ine
                else :
                    if sagesse < 40 :
                        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Sa   
                    elif intelligence < 98 :
                        type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaIne
                    else :
                        type_rune, indicatif, other_rune = selectRune5('refeu')
            elif vita < 426 :
                if vita == 423 and intelligence > 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Ine
                else :
                    if docrit < 15 :
                        type_rune, indicatif, done = selectRune(1,11, data, nom_item) #DoCrit
                    elif dofeu < 19 and docrit != 17 :
                        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoFeu
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
                if esqpm < 7: 
                    type_rune, indicatif, done = selectRune(1,10, data, nom_item) #EsquivPm
                else :
                    type_rune, indicatif, other_rune = selectRune5('refeu')
            return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (pa > 0)  and ( intelligence < 101) and (poid < min):
        type_rune, indicatif, done = selectRune(1,5, data, nom_item) #pa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not crit > 2  and (intelligence < 101):
        type_rune, indicatif, done = selectRune(1, 4, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other, other_rune 

    if not (esqpm > 6 ) and ( intelligence < 101):
        type_rune, indicatif, done = selectRune(2, 10, data, nom_item) #PaRePme
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not sagesse > 29 and ( intelligence < 101):
        type_rune, indicatif, done = selectRune(2, 3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune 

    if not (docrit > 10) and ( intelligence < 101):
        type_rune, indicatif, done = selectRune(2, 11, data, nom_item)  #PaDoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (vita > 289)  and (intelligence < 101) :
        if vita == 0 or (vita > 0 and vita < 266) :
            type_rune, indicatif, done = selectRune(3, 1, data, nom_item) #RaVi
        if (vita > 265 and vita < 290) :
            type_rune, indicatif, done = selectRune(2, 1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (dofeu > 13) and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(2, 7, data, nom_item) #PaDoFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not invo > 0 and ( intelligence < 101)  and (poid < min) :
        type_rune, indicatif, done = selectRune(1, 6, data, nom_item) #Invo
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not intelligence > 79 :
        if (intelligence > 5 and intelligence < 13 ) or (intelligence > 35 and intelligence < 43) or (intelligence > 45 and intelligence < 53) :
            type_rune, indicatif, done = selectRune(2, 2, data, nom_item) #PaIne
        elif (intelligence < 6)  or (intelligence > 12 and intelligence < 36) or (intelligence > 42 and intelligence < 46) or (intelligence > 52 and intelligence < 80) :
            type_rune, indicatif, done = selectRune(3, 2, data, nom_item) #RaIne
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not reperfeu > 7 and ( intelligence < 101):
        type_rune, indicatif, done = selectRune(1, 9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (crit > 4) and ( intelligence < 101):
        if crit < 5 :
            type_rune, indicatif, done = selectRune(1, 4, data, nom_item) #Crit
        if crit > 5 : 
            if docrit < 15 :
                type_rune, indicatif, done = selectRune(1, 11, data, nom_item) #DoCrit
            elif dofeu < 20 :
                type_rune, indicatif, done = selectRune(1, 7, data, nom_item) #DoFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not esqpm > 8 and ( intelligence < 101):
        type_rune, indicatif, done = selectRune(1, 10, data, nom_item) #RePme
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not sagesse > 33 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(2, 3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (intelligence > 91 and intelligence < 101) :
        if intelligence < 101 :
            if intelligence == 91 :
                list_1 = screen(760, 782, 200, 37, 1)
                print('vide :' ,list_1[0])
                if list_1[0] == '\x0c':
                    type_rune, indicatif, done = selectRune(3, 2, data, nom_item) #RaIne                                                                   
                else:
                    if sagesse < 40:
                        type_rune, indicatif, done = selectRune(1, 3, data, nom_item)#Sa
                    else : 
                        type_rune, indicatif, done = selectRune(1, 1, data, nom_item)#Vi
            elif intelligence > 91 and intelligence < 95 :
                type_rune, indicatif, done = selectRune(2, 2, data, nom_item) #RaIne
            elif intelligence < 91 :
                type_rune, indicatif, done = selectRune(3, 2, data, nom_item)  #RaIne                                                                 
        if intelligence > 100 : 
            type_rune, indicatif, other_rune = selectRune5('ini')                                             
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (vita > 389 and vita < 401)  and ( intelligence < 101 ) : 
        if (vita > 289 and vita < 311 ) or (vita > 339 and vita < 390) :
            type_rune, indicatif, done = selectRune(3, 1, data, nom_item) #RaVi
        elif (vita > 310 and vita < 340) :
            type_rune, indicatif, done = selectRune(2, 1, data, nom_item) #PaVi
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not dofeu > 16 and ( intelligence < 101) :
        if dofeu == 14 :
            type_rune, indicatif, done = selectRune(2, 7, data, nom_item) #PaDoFeu
        if dofeu > 14 and dofeu < 17 :
            type_rune, indicatif, done = selectRune(1, 7, data, nom_item) #DoFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not reperfeu > 9 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(1, 9, data, nom_item) #RePerFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not docrit > 13 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(1, 11, data, nom_item) #DoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not esqpm > 9 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(1, 10, data, nom_item) #RePme
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not sagesse > 35 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(2, 3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not (intelligence > 94 and intelligence < 101) :
        if intelligence < 101 :
            if intelligence == 91 :
                list_1 = screen(760, 782, 200, 37, 1)
                print('vide :' ,list_1[0])
                if list_1[0] == '\x0c':
                    type_rune, indicatif, done = selectRune(3, 2, data, nom_item) #RaIne                                                                   
                else:
                    if sagesse < 40:
                        type_rune, indicatif, done = selectRune(1, 3, data, nom_item)#Sa
                    else : 
                        type_rune, indicatif, done = selectRune(1, 1, data, nom_item)#Vi
            if intelligence > 91 and intelligence < 95 :
                type_rune, indicatif, done = selectRune(2, 2, data, nom_item) #PaIne
            else :
                type_rune, indicatif, done = selectRune(3, 2, data, nom_item)  #RaIne                                                                 
        if intelligence > 100 : 
            type_rune, indicatif, other_rune = selectRune5('ini')                                             
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not docrit > 14 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(1, 11, data, nom_item) #DoCrit
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not  dofeu > 19 and ( intelligence < 101) :
        if dofeu == 17 :
            type_rune, indicatif, done = selectRune(2, 7, data, nom_item) #PaDoFeu
        if dofeu == 18 or dofeu == 19 :
            type_rune, indicatif, done = selectRune(1, 7, data, nom_item) #DoFeu
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if not sagesse > 37 and ( intelligence < 101) :
        type_rune, indicatif, done = selectRune(2, 3, data, nom_item) #PaSa
        return type_rune, indicatif, done, tenta, poid, other, other_rune

    if near_perf:
            if mode == "reperfeu":
                type_rune = 6
                if type_rune <= poid:
                    type_rune, indicatif, done = selectRune(1, 9, data, nom_item) #RePerFeu
                    return type_rune, indicatif, done, tenta, poid, other, other_rune
                if reperfeu > 10 and reperfeu < 13:
                    if double_exo == 1 :
                        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                        if list_1[0].find('Po') == -1 or list_1[1].find('Po') == -1:
                            type_rune, indicatif, other_rune = selectRune5('po')
                            time.sleep(1)
                        else :
                            other = OtherItem(nombre_item)(nombre_item)
                            other = True
                        return type_rune, indicatif, done, tenta, poid, other, other_rune
                    else :
                        if nombre_item > 1:
                            other = OtherItem(nombre_item)(nombre_item)
                            type_rune, indicatif = 0, 7
                            return type_rune, indicatif, done, tenta, poid, done, other_rune
                        else :
                            type_rune, indicatif, done = 0, 7, True
                            return type_rune, indicatif, done, tenta, poid, done, other_rune
                else :
                    other = OtherItem(nombre_item)(nombre_item)
                    type_rune, indicatif = 0, 7
                    return type_rune, indicatif, done, tenta, poid, done, other_rune

            if mode == "overvita" and poid > min:
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
                    other = OtherItem(nombre_item)(nombre_item)
                    type_rune, indicatif, poid = 0, 7, 0
                    return type_rune, indicatif, done, tenta, poid, done, other_rune

            elif mode == "overvita" and poid <= min :
                if vita < 450 :
                    # list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
                    # if list_value[0].find('Po') == -1:
                    #     type_rune, indicatif, other_rune = selectRune5('po')
                    #     return type_rune, indicatif, done, tenta, poid, other, other_rune
                    # else :
                    other = OtherItem(nombre_item)(nombre_item)
                    type_rune, indicatif, poid = 0, 7, 0
                    return type_rune, indicatif, done, tenta, poid, done, other_rune
                else :
                    other = OtherItem(nombre_item)(nombre_item)
                    type_rune, indicatif, poid = 0, 7, 0
                    return type_rune, indicatif, done, tenta, poid, done, other_rune

            if mode == "dosort" :
                if vita < 399  and poid%min >= 3:
                    type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
                    return type_rune, indicatif, done, tenta, poid, other, other_rune
                if vita < 396 and poid%min >= 1:
                    type_rune, indicatif, done = selectRune(1,1, data, nom_item) #PaVi
                    return type_rune, indicatif, done, tenta, poid, other, other_rune
                type_rune = 15 
                if type_rune <= poid :
                    type_rune, indicatif, other_rune = selectRune5('dosort')
                    return type_rune, indicatif, done, tenta, poid, other, other_rune
                list_value = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
                if list_value[0].find('% Dommages aux sorts') != -1:
                    other = OtherItem(nombre_item)(nombre_item)
                    type_rune, indicatif, poid = 0, 7, 0
                else :
                    type_rune, indicatif, other_rune = selectRune5('po')
                    indicatif = 7
                return type_rune, indicatif, done, tenta, poid, done, other_rune                 