import time
from pyautogui import scroll
from Macro1 import * 
from screen import screenValues
from MainScreen import screen
from Reconnect import *

def UpStats2(list_value, poid, nombre_item, nombre_ligne_item, tenta, nom_item, pui, tenta_plus, other):
    import json
    from pathlib import Path
  # attribuation des variables en fonction de leur ligne
    other, done = False, False
    path_item = Path("..").resolve()
    path = path_item / "DictionnaireItem/item.json"
    with open(path, encoding='utf-8') as outfile:
        data =json.load(outfile)
    A = int(list_value[0])
    B = int(list_value[1])
    C = int(list_value[2])
    D = int(list_value[3])
    E = int(list_value[4])
    F = int(list_value[5])
    G = int(list_value[6])
    H = int(list_value[7])
    I = int(list_value[8])
    J = int(list_value[9])
    K = int(list_value[10])
    L = int(list_value[11])
    M = int(list_value[12])
    near_perf = (A > 92 and B > 57 and C > 57 and D > 32 and E > 5 and G > 0 and H > 5 and I > 5 and J > 7 and K > 9 and L > 9 and M > 10 )
    perf = (A > 94 and B > 57 and C > 57 and D > 33 and E > 5 and G > 0 and H > 6 and I > 6 and J > 7 and K > 9 and L > 9 and M > 11 )
    exo =0

    if nombre_ligne_item > 12 :
        nombre_ligne_item = 10

    if not (F > 0)  and ((A < 101 and B < 61 and C < 61) and poid < 3) or (near_perf and (poid >2.9 and poid <5 and F < 1)) or M >13: #portée
    # if not (F > 0)  and (A < 101 and B < 61 and C < 61)  :
        type_rune, indicatif, done = selectRune(1,6, data, nom_item) #Portée
        time.sleep(2.5)
        return type_rune, indicatif, done, tenta, other, poid
    if not (G > 0) and (A < 101 and B < 61 and C < 61): #invoc
        type_rune, indicatif, done = selectRune(1,7, data, nom_item) #Invo
        time.sleep(2.5)
        return type_rune, indicatif, done, tenta, other, poid
    if not A > 59 and (A < 101 and B < 61 and C < 61): #vitalité
        type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        return type_rune, indicatif, done, tenta, other, poid
    if not (E > 3) and (A < 101 and B < 61 and C < 61): #critique
        type_rune, indicatif, done = selectRune(1,5, data, nom_item) #Crit
        return type_rune, indicatif, done, tenta, other, poid
    if not K > 5 and (A < 101 and B < 61 and C < 61): # ReTerre
        type_rune, indicatif, done = selectRune(2,11, data, nom_item) #PaReTerre
        return type_rune, indicatif, done, tenta, other, poid
    if not H > 3 and (A < 101 and B < 61 and C < 61):
        type_rune, indicatif, done = selectRune(2,8, data, nom_item) #PaDoFeu
        return type_rune, indicatif, done, tenta, other, poid
    if not D > 28 and (A < 101 and B < 61 and C < 61):
        if D < 20 :
            type_rune, indicatif, done = selectRune(3,4, data, nom_item)
        if D > 19 : #PaSa
            type_rune = 9 
            type_rune, indicatif, done = selectRune(2,4, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not J > 5 and (A < 101 and B < 61 and C < 61):
        type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerEau
        return type_rune, indicatif, done, tenta, other, poid
    if not M > 8 and (A < 101 and B < 61 and C < 61):
        type_rune, indicatif, done = selectRune(2,13, data, nom_item) #PaDoCrit
        return type_rune, indicatif, done, tenta, other, poid
    if not L > 5 and (A < 101 and B < 61 and C < 61): # ReAir
        type_rune, indicatif, done = selectRune(2,12, data, nom_item) #PaReAir
        return type_rune, indicatif, done, tenta, other, poid
    if not B > 46 and (A < 101 and B < 61 and C < 61):  #Intel
        if B == 10 or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) :
            type_rune, indicatif, done = selectRune(3,2, data, nom_item)
        if B < 10 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40) :
            type_rune, indicatif, done = selectRune(2,2, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not C > 46 and (A < 101 and B < 61 and C < 61):  #agilité
        if C == 10 or (C > 17 and C < 21) or (C > 27 and C < 31) or (C > 37 and C < 41) :
            type_rune, indicatif, done = selectRune(3,3, data, nom_item)
        if C < 10 or (C > 10 and C < 18) or (C > 20 and C < 28) or (C > 30 and C < 38) or (C > 40) :
            type_rune, indicatif, done = selectRune(2,3, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not I > 3 and (A < 101 and B < 61 and C < 61): #Dommage Air
        type_rune, indicatif, done = selectRune(2,9, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid ### fin étape 1
    if not E > 4 and (A < 101 and B < 61 and C < 61): #critique
        type_rune, indicatif, done = selectRune(1,5, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not K > 6 and (A < 101 and B < 61 and C < 61): #ReTerre
        type_rune, indicatif, done = selectRune(2,11, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not A > 79 and (A < 101 and B < 61 and C < 61): #Vitalité
        type_rune, indicatif, done = selectRune(2,1, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not M > 9 and (A < 101 and B < 61 and C < 61):
        type_rune, indicatif, done = selectRune(1,13, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not D > 32 and (A < 101 and B < 61 and C < 61): #Sagesse
        type_rune, indicatif, done = selectRune(2,4, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not J > 6 and (A < 101 and B < 61 and C < 61): #Resistance Eau%
        type_rune, indicatif, done = selectRune(1,10, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not (B > 55 and B < 61)  and (A < 101 and C < 61): 
        indicatif = 1
        if (B > 47 and B < 53) : #Intel
            type_rune, indicatif, done = selectRune(3,2, data, nom_item)
        if (B > 52 and B < 61)or B == 47:
            type_rune, indicatif, done = selectRune(2,2, data, nom_item)
        if (B > 60 and B < 62):
            if C < 60 : 
                type_rune, indicatif, done = selectRune(1,3, data, nom_item)
            elif A < 96 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item)
            elif K < 10 :
                type_rune, indicatif, done = selectRune(1,11, data, nom_item)
            elif L < 10 :
                type_rune, indicatif, done = selectRune(1,12, data, nom_item)  
            else : 
                type_rune, indicatif, other_rune = selectRune5('ini')                                                                         
        if B > 61 :
            if C < 58:
                type_rune, indicatif, done = selectRune(2,3, data, nom_item)
            elif A < 86:
                type_rune, indicatif, done = selectRune(2,1, data, nom_item)
            elif K < 10 :
                type_rune, indicatif, done = selectRune(1,11, data, nom_item)
            elif L < 10 :
                type_rune, indicatif, done = selectRune(1,12, data, nom_item)  
            else :
                type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, other, poid
    if not (C > 55 and C < 61)  and (A < 101 and B < 61): 
        indicatif = 2
        if (C > 47 and C < 53) : #Agilité
            type_rune, indicatif, done = selectRune(3,3, data, nom_item)
        if (C > 52 and C < 61) or C == 47:
            type_rune, indicatif, done = selectRune(2,3, data, nom_item)
        if (C > 60 and C < 62):
            if B < 60 : 
                type_rune, indicatif, done = selectRune(1,2, data, nom_item)
            elif A < 96 :
                type_rune, indicatif, done = selectRune(1,1, data, nom_item)
            elif K < 10 :
                type_rune, indicatif, done = selectRune(1,11, data, nom_item)
            elif L < 10 :
                type_rune, indicatif, done = selectRune(1,12, data, nom_item)  
            else : 
                type_rune, indicatif, other_rune = selectRune5('ini')                                                                                
        if C > 61 :
            if B < 58:
                type_rune, indicatif, done = selectRune(2,2, data, nom_item)
            elif A < 86:
                type_rune, indicatif, done = selectRune(2,1, data, nom_item)
            elif K < 10 :
                type_rune, indicatif, done = selectRune(1,11, data, nom_item)
            elif L < 10 :
                type_rune, indicatif, done = selectRune(1,12, data, nom_item)  
            else :
                type_rune = 2
                type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, other, poid
    if not I > 5 and (A < 101 and B < 61 and C < 61): # Dommage Air
        type_rune, indicatif, done = selectRune(1,9, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not H > 5 and (A < 101 and B < 61 and C < 61): # Dommage Feu
        type_rune, indicatif, done = selectRune(1,8, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not L > 7 and (A < 101 and B < 61 and C < 61): #Resistance Air
        if L == 6 :
            type_rune, indicatif, done = selectRune(2,12, data, nom_item)
        if L > 6 :
            type_rune, indicatif, done = selectRune(1,12, data, nom_item)
        return type_rune, indicatif, done, tenta, other, poid
    if not (E > 5 and E < 7) and (A < 101 and B < 61 and C < 61): #Critique
        if E < 7 :
            type_rune, indicatif, done = selectRune(1,5, data, nom_item)
        if E > 6 :
            if D < 38 :
                type_rune, indicatif, done = selectRune(2,4, data, nom_item)
            else : 
                type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, other, poid
    if not (A > 92 and A < 101) : #Vitalité
        if A > 79 and A < 93 :
            type_rune, indicatif, done = selectRune(2,1, data, nom_item)
        elif A > 100 :
            if A > 100 and A < 106 :
                if B < 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item)
                elif C < 60:
                    type_rune, indicatif, done = selectRune(1,3, data, nom_item)
                else :
                    type_rune, indicatif, other_rune = selectRune5('ini')
            if A > 105 :
                if K < 10 :
                    type_rune, indicatif, done = selectRune(1,11, data, nom_item)
                elif L < 10 :
                    type_rune, indicatif, done = selectRune(1,12, data, nom_item)
                elif B < 60:
                    type_rune, indicatif, done = selectRune(1,2, data, nom_item)
                elif C < 60:
                    type_rune, indicatif, done = selectRune(1,3, data, nom_item)
                else : 
                    type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, other, poid
    if not (L > 9 and L < 11) and (A < 101 and B < 61 and C < 61): #Resistance Air
        if L < 11 :
            type_rune, indicatif, done = selectRune(1,12, data, nom_item)
        if L > 10 :
            type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, other, poid
    if not (K > 9 and K < 11) and (A < 101 and B < 61 and C < 61): #Resistance Terre
        if K <11 :
            type_rune, indicatif, done = selectRune(1,11, data, nom_item)
        if K > 10 :
            type_rune, indicatif, other_rune = selectRune5('refeu')
        return type_rune, indicatif, done, tenta, other, poid 
    if not J > 7 and (A < 101 and B < 61 and C < 61): #Resistance Eau%
        type_rune, indicatif, done = selectRune(1,10, data, nom_item)   
        return type_rune, indicatif, done, tenta, other, poid
    if not M > 10 and (A < 101 and B < 61 and C < 61):  #Dommage Critique
        type_rune, indicatif, done = selectRune(1,13, data, nom_item) 
        return type_rune, indicatif, done, tenta, other, poid
    if A > 92 and B > 55 and C > 55 and D > 32 and E > 5  and G > 0 and H > 5 and I > 5 and J > 7 and K > 9 and L > 9 and M > 10 :
        type_rune = 9
        if not D > 34 and type_rune <= poid :
            type_rune, indicatif, done = selectRune(2,4, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid
        type_rune = 5
        if not M > 11 and type_rune <= poid :
            type_rune, indicatif, done = selectRune(1,13, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid                                                                      
        type_rune = 5
        if not H > 6 and type_rune <= poid :
            type_rune, indicatif, done = selectRune(1,8, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid
        type_rune = 5
        if not I > 6 and type_rune <= poid :
            type_rune, indicatif, done = selectRune(1,9, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid
        type_rune = 3
        if not B > 57 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(2,2, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid
        type_rune = 3
        if not C > 57 and type_rune <= poid:
            type_rune, indicatif, done = selectRune(2,3, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid
        type_rune = 9
        if not D > 36 and type_rune <= poid :
            type_rune, indicatif, done = selectRune(2,4, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid
        type_rune = 5
        if not M > 13 and type_rune <= poid :
            type_rune, indicatif, done = selectRune(1,13, data, nom_item)
            return type_rune, indicatif, done, tenta, other, poid   

        # type_rune = 6
        # if type_rune <= poid :  
        #     time.sleep(0.2)
        #     Scroll('down')
        #     list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
        #     Scroll('up')
        #     indicatif = 0                                                                                                                                                            
        #     if not list_1[0].find('Air') != -1  and type_rune <= poid:
        #         type_rune, indicatif, other_rune = selectRune5('reperair')
        #         return type_rune, indicatif, done, tenta, other, poid
        #     else : 
        #         poid = 0
        #         exo = 1 
        #         print('here')
        #         suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
        #         return type_rune, indicatif, done, tenta, other, poid
        else :
            if A > 92 and B > 55 and C > 55 and D > 32 and E > 5 and F > 0 and G > 0 and H > 5 and I > 5 and J > 7 and K > 9 and L > 9 and M > 10 :
                indicatif = 0
                time.sleep(0.2)
                Scroll('down')                                                                                                                                
                list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                Scroll('up')
                time.sleep(0.3)
                if list_1[1].find('Tacle') != -1 and list_1[0].find('Critiques') != -1:
                    type_rune = 90
                    if sum(pui) >= 595 :
                        tenta_plus +=1
                    tenta += 1
                    if exo != 1:
                        suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                    if perf:
                        print('balise 1')
                        other = OtherItem(nombre_item)
                        indicatif, type_rune = 0, 90
                        return type_rune, indicatif, done, tenta, True, poid
                    else :
                        print('balise 10')
                        type_rune, indicatif, other_rune = selectRune5('pm')
                        return type_rune, indicatif, done, tenta, other, poid                                  
                elif list_1[0].find('PA') != -1 or  list_1[0].find('1PM') != -1 or list_1[1].find('PA') != -1 or  list_1[1].find('1PM') != -1 :
                    type_rune = 0
                    print('balise 2')
                    other = OtherItem(nombre_item)
                    return type_rune, indicatif, done, tenta, True, poid
                else :
                    type_rune = 90
                    if sum(pui) >= 595 :
                        tenta_plus += 1
                    tenta += 1
                    if exo != 1:
                        suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
                    if perf:
                        print('balise 3')
                        other = OtherItem(nombre_item)
                        indicatif = 0
                        return type_rune, indicatif, done, tenta, True, poid
                    else :
                        print('balise 20')
                        type_rune, indicatif, other_rune = selectRune5('pm')
                        scroll('down')
                        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                        scroll('up')
                        if list_1[0].find('PA') != -1 or  list_1[0].find('PM') != -1 :
                            print('balise 4')
                            other = OtherItem(nombre_item)
                return type_rune, indicatif, done, tenta, True, poid