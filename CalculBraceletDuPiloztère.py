import time
from Macro1 import * 
from screen import screenValues
from MainScreen import screen
from Reconnect import *
import re
import json

def UpStats(list_value, poid, nombre_item, nombre_ligne_item, tenta, nom_item, mode, other, pui, tenta_po):
    from pathlib import Path
    # attribuation des variables en fonction de leur ligne
    done =  False
    tenta_plus, exo = 0, 0
    vita = int(list_value[0])
    puissance = int(list_value[1])
    crit = int(list_value[2])
    po = int(list_value[3])
    doneutre = int(list_value[4])
    doterre = int(list_value[5])
    doeau = int(list_value[6])
    reperneutre = int(list_value[7])
    under1_root_path = Path("..").resolve()
    path_dict_item = under1_root_path / "DictionnaireItem/item.json"
    with open(path_dict_item, encoding='utf-8') as outfile:
        data =json.load(outfile)
    near_perf = (vita>289 and puissance>45 and crit == 4 and doneutre > 7 and doterre>7 and doeau>7 and reperneutre== 10)
    perf = (vita > 293 and puissance > 47 and po ==2 and crit ==4 and doneutre == 10 and doterre ==10 and doeau ==10 and reperneutre ==10)
    if vita > 300 and not near_perf: 
        if vita < 306 :
            type_rune, indicatif, other_rune = selectRune5('ini')
        elif vita < 311:
            if puissance< 50:
                type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Pui
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        elif vita < 316:
            if vita == 312 or vita == 313:
                type_rune, indicatif, other_rune = selectRune5('pod')
            else :
                type_rune, indicatif, other_rune = selectRune5('ini')
        elif vita < 321:
            if vita == 318 or vita ==317:
                type_rune, indicatif, other_rune = selectRune5('pod')
            else :
                type_rune, indicatif, other_rune = selectRune5('ini')
        elif vita < 326:
            if vita == 324 or vita == 325:
                if doterre< 8:
                    type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoTerre
                elif doneutre < 8:
                    type_rune, indicatif, done = selectRune(1,5, data, nom_item) #DoNeutre
                elif doeau< 8:
                    type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau

                elif doterre< 9:
                    type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoTerre
                elif doneutre < 9:
                    type_rune, indicatif, done = selectRune(1,5, data, nom_item) #DoNeutre
                elif doeau< 9:
                    type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau

                elif doterre< 10:
                    type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoTerre
                elif doneutre < 10:
                    type_rune, indicatif, done = selectRune(1,5, data, nom_item) #DoNeutre
                elif doeau< 10:
                    type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        elif vita < 400:
            if reperneutre< 10:
                type_rune, indicatif, done = selectRune(1,8, data, nom_item) #RePerNeutre
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if mode == "overvita" :
        min = 1
    if mode == "docrit":
        min = 5
    if not (po> 1)  and poid < min:  ###1###1### Portée
        type_rune, indicatif, done = selectRune(1,4, data, nom_item)
        time.sleep(1.5)
        if po == 1:
            tenta_po +=1
            rune = screenValues(290, 852, 285, 38, 1)
            print('rune Po :', rune)
            if rune[0]== '1 Portée\n\x0c' or rune[0]== '1 Portée\n':
                value ="|SC"
            else :
                value ="| SN/ECHEC"
            suivis_more_value(list_value, tenta, pui, nom_item, exo, data, value,tenta_po, nombre_ligne_item)
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not crit > 2 : ###1###2### Crit
        type_rune, indicatif, done = selectRune(1,3, data, nom_item)
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not reperneutre> 6 :  ###1###3### % Résistance neutre
        type_rune, indicatif, done = selectRune(1,8, data, nom_item)
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not puissance > 39 :  ###1###4### Puissance
        if puissance == 0 or puissance == 10 or puissance == 20 or puissance  == 30 or puissance > 37 :
            type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaPui
        else :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item)  #PaPui  
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doeau> 5 :  ###1###5### Dommages Eau
        if doeau== 1 :
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau  
        else : 
            type_rune, indicatif, done = selectRune(2,7, data, nom_item)  #PaDoEau
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not vita > 239 :  ###1###6### Vita
        if (vita == 0 ) or (vita > 0 and vita < 101) or (vita > 144 and vita < 165) or (vita > 189 and vita < 201):
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) # ravi
        if (vita > 100 and vita < 145) or (vita > 164 and vita < 190) or (vita > 200 and vita < 240):
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) # pa vi
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doterre> 5 :  ###1###7### Dommages Terre
        if doterre== 1 :
            type_rune, indicatif, done = selectRune(1,6, data, nom_item)   #DoTerre
        else : 
            type_rune, indicatif, done = selectRune(2,6, data, nom_item)  #PaDoTerre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doneutre > 5 :  ###1###8### Dommages Neutre
        if doneutre == 1 :
            type_rune, indicatif, done = selectRune(1,5, data, nom_item)  #DoNeutre
        else :  
            type_rune, indicatif, done = selectRune(2,5, data, nom_item)  #PaDoNeutre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not crit > 3 : ###2###1### Crit
        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not puissance > 45 :  ###2###2### Puissance
        if puissance == 40:
            type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaPui
        else :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item)  #PaPui
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not vita > 293 :  ###2###3### Vita
        if (vita > 239 and vita < 260) or (vita > 270 and vita < 275) or (vita > 285 and vita < 290):
            type_rune, indicatif, done = selectRune(3,1, data, nom_item) # RaVi
        if (vita > 259 and vita < 271) or (vita > 274 and vita < 286) or vita > 289: 
            type_rune, indicatif, done = selectRune(2,1, data, nom_item) # PaVi
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not reperneutre> 9 :  ###2###4### % Résistance neutre
        type_rune, indicatif, done = selectRune(1,8, data, nom_item) #RePerNeutre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doneutre > 7 :  ###2###5### Dommages Neutre
        if doneutre == 6 :
            type_rune, indicatif, done = selectRune(2,5, data, nom_item)  #PaDoNeutre
        else : 
            type_rune, indicatif, done = selectRune(1,5, data, nom_item) #DoNeutre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doterre> 7  :  ###2###6### Dommages Terre
        if doterre== 6 :
            type_rune, indicatif, done = selectRune(2,6, data, nom_item)  #PaDoTerre
        else : 
            type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoTerre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doeau> 7 :  ###2###7### Dommages Eau
        if doeau== 6 :
            type_rune, indicatif, done = selectRune(2,7, data, nom_item) #PaDoEau
        else : 
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau
        return type_rune, indicatif, done, tenta, poid, other, tenta_po

    if not doneutre > 8 :  ###2###5### Dommages Neutre
        if doneutre == 6 :
            type_rune, indicatif, done = selectRune(2,5, data, nom_item)  #PaDoNeutre
        else : 
            type_rune, indicatif, done = selectRune(1,5, data, nom_item) #DoNeutre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doterre> 8  :  ###2###6### Dommages Terre
        if doterre== 6 :
            type_rune, indicatif, done = selectRune(2,6, data, nom_item)  #PaDoTerre
        else : 
            type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoTerre
        return type_rune, indicatif, done, tenta, poid, other, tenta_po
    if not doeau> 8 :  ###2###7### Dommages Eau
        if doeau== 6 :
            type_rune, indicatif, done = selectRune(2,7, data, nom_item) #PaDoEau
        else : 
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau
        return type_rune, indicatif, done, tenta, poid, other, tenta_po

    if ((vita > 289 ) and (puissance > 45 ) and (crit > 3)  and (doneutre > 7) and (doterre> 7) and ( doeau> 7) and (reperneutre>  9)) :
        type_rune = 6
        if not puissance > 47 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaPui
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 5
        if not doneutre > 8 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(1,5, data, nom_item) # DoNeutre
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 5
        if not doterre> 8 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(1,6, data, nom_item) # DoTerre
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 5
        if not doeau> 8 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 6
        if not puissance > 46 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(2,2, data, nom_item) # PaPui
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 5
        if not doneutre > 9 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(1,5, data, nom_item) # DoNeutre
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 5
        if not doterre> 9 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoTerre
            return type_rune, indicatif, done, tenta, poid, other, tenta_po
        type_rune = 5
        if not doeau> 9 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoEau
            return type_rune, indicatif, done, tenta, poid, other, tenta_po

        if poid < min and perf:
            OtherItem(nombre_item)
            type_rune = 0 
            indicatif = 0
            poid = 0
            return type_rune, indicatif, done, tenta, 0, True, tenta_po
        if mode == 'overvita' :
            if poid >=min :
                type_rune = 10
                if not vita >305 and type_rune < poid :
                    type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
                    return type_rune, indicatif, done, tenta, poid, other, tenta_po
                type_rune = 3
                if not vita > 340 and type_rune <poid :
                    type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
                    return type_rune, indicatif, done, tenta, poid, other, tenta_po
                type_rune = 1
                if not vita > 350 :
                    type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vi
                    return type_rune, indicatif, done, tenta, poid, other, tenta_po
                else :
                    docrit_screen = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                    if docrit_screen[0].find('PA') != -1 or docrit_screen[0].find('PM') != -1 or docrit_screen[1].find('PA') != -1 or docrit_screen[1].find('PM') != -1 :
                        OtherItem(nombre_item)
                        type_rune = 0 
                        indicatif = 0
                        return type_rune, indicatif, done, tenta, 0, True, tenta_po
                    else :
                        tenta+=1
                        suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                        type_rune, indicatif, other_rune = selectRune5('pm') #Pm 
                        return type_rune, indicatif, done, tenta, poid, other, tenta_po
            else : 
                docrit_screen = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                if docrit_screen[0].find('PA') != -1 or docrit_screen[0].find('PM') != -1 or docrit_screen[1].find('PA') != -1 or docrit_screen[1].find('PM') != -1 :
                    OtherItem(nombre_item)
                    type_rune = 0 
                    indicatif = 0
                    return type_rune, indicatif, done, tenta, 0, True, tenta_po
                else :
                    exo = f'{vita-300} over'
                    tenta+=1
                    suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                    if vita-300 > 5:
                        type_rune, indicatif, other_rune = selectRune5('pm') #Pm 
                    else :
                        type_rune, indicatif, other_rune = selectRune5('pa') #Pa
                    return type_rune, indicatif, done, tenta, poid, other, tenta_po

        if mode == "docrit" :
            if poid >= min:
                docrit_screen = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                print('exo screen :', docrit_screen)
                if docrit_screen[0].find('2 Dommages Critiques') != -1 :
                    exo = '2 DoCrit'
                    type_rune = 0 
                    indicatif = 0
                    return type_rune, indicatif, done, tenta, 0, other, tenta_po
                    if docrit_screen[1] != '':
                        OtherItem(nombre_item)
                        type_rune = 0 
                        indicatif = 0
                        print('balise 1')
                        return type_rune, indicatif, done, tenta, 0, True, tenta_po
                    else :
                        print('balise 2')
                        OtherItem(nombre_item)
                        type_rune = 0 
                        indicatif = 0
                        return type_rune, indicatif, done, tenta, 0, True, tenta_po
                        # tenta +=1
                        # suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                        # type_rune, indicatif, other_rune = selectRune5('pm') #Pm 
                        # poid += 10
                        # return type_rune, indicatif, done, tenta, poid, other, tenta_po
                else :
                    if docrit_screen[0].find('PA') != -1 or docrit_screen[0].find('PM') != -1 or docrit_screen[1].find('PA') != -1 or docrit_screen[1].find('PM') != -1 :
                        print('balise 3')
                        OtherItem(nombre_item)
                        type_rune = 0 
                        indicatif = 0
                        return type_rune, indicatif, done, tenta, 0, True, tenta_po
                    else :
                        print('balise 4')
                        type_rune, indicatif, other_rune = selectRune5('docrit') #DoCrit
                        return type_rune, indicatif, done, tenta, poid, other, tenta_po
            else :
                docrit_screen = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                if docrit_screen[0].find('Dommages Critiques') != -1 :
                    print('balise 5')
                    OtherItem(nombre_item)
                    type_rune = 0 
                    indicatif = 0
                    return type_rune, indicatif, done, tenta, 0, True, tenta_po
                number = re.sub("[^0-9]","", docrit_screen[0])
                if docrit_screen[0] != "":
                    if docrit_screen[0].find('PA') != -1 or docrit_screen[0].find('PM') != -1 or docrit_screen[1].find('PA') != -1 or docrit_screen[1].find('PM') != -1 :
                        type_rune = 0 
                        indicatif = 0
                        print('balise 6')
                        OtherItem(nombre_item)
                        return type_rune, indicatif, done, tenta, 0, True, tenta_po
                    else :
                        print('balise 7')
                        docrit_screen = clean_string(docrit_screen)
                        exo = str(number)+' '+ str(docrit_screen[0])
                        tenta +=1
                        suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                        type_rune, indicatif, other_rune = selectRune5('pm') #Pm 
                        if docrit_screen[0] == '':
                            pass
                        else :
                            poid += int(data['dict_poid_ligne'][docrit_screen[0]])*int(number)
                        return type_rune, indicatif, done, tenta, poid, other, tenta_po
                else:
                    print('balise 8')
                    exo = 'near perf'
                    tenta +=1
                    suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                    type_rune, indicatif, other_rune = selectRune5('pm') #Pm 
                    return type_rune, indicatif, done, tenta, poid, other, tenta_po