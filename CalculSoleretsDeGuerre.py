import time
from MainScreen import *
import re
from Macro1 import * 

def UpStats(list_value, poid, nombre_item,pui, nombre_ligne_item):
    try :
        A = int(list_value[0])
        B = int(list_value[1])
        C = int(list_value[2])
        D = int(list_value[3])
        E = int(list_value[4])
        F = int(list_value[5])
        G = int(list_value[6])
        H = int(list_value[7])
        I = int(list_value[8])
        K = int(list_value[10])
        L = int(list_value[11])
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return type_rune, indicatif, False

    if not (E > 0)  and (A < 401 and B < 101) and (poid <6): #Pm
        indicatif = 4
        type_rune = 90
        selectRune(1,5)
        return type_rune, indicatif, False
    if not D > 1  and (A < 401 and B < 101):
        indicatif = 3
        type_rune = 10
        selectRune(1, 4) #Crit
        return type_rune, indicatif, False
    if not (K > 6 ) and (A < 401 and B < 101):
        indicatif = 10
        type_rune = 21
        selectRune(2, 11) #PaRetPm
        return type_rune, indicatif, False
    if not C > 19 and (A < 401 and B < 101):
        indicatif = 2
        type_rune = 9
        selectRune(2, 3) #PaSa
        return type_rune, indicatif, False 
    if not (L > 10) and (A < 401 and B < 101):
        indicatif = 11
        type_rune = 15
        selectRune(2, 12)  #PaDoCrit
        return type_rune, indicatif, False
    if not (A > 289)  and (B < 101) :
        indicatif = 0
        if A == 0 or (A > 0 and A < 266) :
            type_rune = 10
            selectRune(3, 1) #RaVi
        if (A > 265 and A < 290) :
            type_rune = 3
            selectRune(2, 1) #PaVi
        return type_rune, indicatif, False
    if not (G > 5) and (A < 401 and B < 101) :
        indicatif = 6
        type_rune = 6
        selectRune(1, 7) #RePerNeu
        return type_rune, indicatif, False
    if not H > 5 and (A < 401 and B < 101) :
        indicatif = 7
        type_rune = 6
        selectRune(1, 8) #RePerEau
        return type_rune, indicatif, False
    if not B > 79 and A < 401 :
        indicatif = 1
        if (B > 5 and B < 13 ) or (B > 35 and B < 43) or (B > 45 and B < 53) :
            type_rune = 3
            selectRune(2, 2) #PaIne
        elif (B < 6)  or (B > 12 and B < 36) or (B > 42 and B < 46) or (B > 52 and B < 80) :
            type_rune = 10
            selectRune(3, 2) #RaIne
        return type_rune, indicatif, False
    if not F > 13 and (A < 401 and B < 101):
        indicatif = 5
        type_rune = 15
        selectRune(2, 6) #PaDoFeu
        return type_rune, indicatif, False
    if not I > 13  and ( A < 401 and B < 101) : 
        indicatif = 8 
        type_rune = 12 
        selectRune(2, 9) #Patacle
        return type_rune, indicatif, False
        #Fin étape 1 
    if not (D > 3) and (A < 401 and B < 101):
        indicatif = 3
        if D < 4 :
            type_rune = 10
            selectRune(1, 4) #Crit
        if D > 4 : 
            if L < 15 :
                indicatif = 11
                type_rune = 5
                selectRune(1, 12) #DoCrit
            elif F < 20 :
                indicatif = 5
                type_rune = 5
                selectRune(1, 6) #DoFeu
        return type_rune, indicatif, False
    if not C > 25 and (A < 401 and B < 101) :
        indicatif = 2
        type_rune = 9
        selectRune(2, 3) #PaSa
        return type_rune, indicatif, False
    if not (B > 91 and B < 101) and (A < 401 ) :
        indicatif = 1
        if B < 101 :
            if B == 91 :
                list_1 = screen(760, 340+40*nombre_ligne_item, 200, 37, 1)
                print('vide :' ,list_1[0])
                if list_1[0] == '\x0c':
                    indicatif = 1
                    type_rune = 10
                    selectRune(3, 2) #RaIne                                                                
                else:
                    if C < 30:
                        indicatif = 2
                        type_rune = 3 #Sa
                        selectRune(1, 3)
                    else : 
                        indicatif = 0 
                        type_rune = 1
                        selectRune(1, 1) #Vi
            else :
                type_rune = 10
                selectRune(3, 2)   #RaIne                                                                 
        if B > 100 : 
            type_rune = 1
            selectRune(1,1)   #vi                                             
        return type_rune, indicatif, False
    if not F > 16 and (A < 401 and B < 101) :
        indicatif = 5
        if F == 14 :
            type_rune = 15
            selectRune(2, 6) #PaDoFeu
        if F > 14 and G < 17 :
            type_rune = 5
            selectRune(1, 6) #DoFeu
        return type_rune, indicatif, False
    if not I > 16 and (A < 401 and B < 101) :
        indicatif = 8
        if I == 14 :
            type_rune = 12
            selectRune(2, 9) #PaTac
        if I > 14 and I < 17 :
            type_rune = 4
            selectRune(1, 9) #Tacle
        return type_rune, indicatif, False
    if not L > 14 and (A < 401 and B < 101) :
        indicatif = 11
        if L < 15 :
            if L == 11:
                type_rune = 15
                selectRune(2, 12)
            else :
                type_rune = 5
                selectRune(1, 12) #DoCrit
        if L > 15 : 
            type_rune = 2
            selectRune5(1075, 1030)
            CleanRune()
        return type_rune, indicatif, False
    if not (A > 389 and A < 401)  and ( B < 101 ): 
        indicatif =  1
        if (A > 289 and A < 311 ) or (A > 339 and A < 390) :
            type_rune = 10
            selectRune(3, 1) #RaVi
        elif (A > 310 and A < 340) :
            type_rune = 3
            selectRune(2, 1) #PaVi
        elif A > 400 and A < 406 :
            indicatif = 1
            if  B < 100 :
                type_rune = 1
                selectRune(1, 2) #Ine
            else : 
                type_rune = 1
                selectRune5(1030, 1030)
                CleanRune()
        elif A > 405 and A < 411 :
            type_rune = 1
            selectRune5(1075, 1030) #ReFeu
            CleanRune()
        elif (A > 410 and A < 416 ) :
            if  C < 40:
                indicatif = 2
                type_rune = 3
                selectRune(1, 3) #Sa
            else : 
                type_rune = 2
                selectRune5(1075, 1030) #ReFeu
                CleanRune()
        elif (A > 415 and A < 421):
            type_rune = 4
            indicatif = 8
            if I < 20 :
                selectRune(1, 9) #Tacle
            else : 
                type_rune =2 
                selectRune5(1075, 1030)
                CleanRune()
        elif (A > 420 and A < 426):
            if L < 15 :
                indicatif = 11
                type_rune = 5
                selectRune(1, 11) #DoCrit                                         
            elif F < 20 :
                indicatif = 5
                type_rune = 5
                selectRune(1, 6) #DoFeu
            else : 
                if I < 20 :
                    indicatif = 8 
                    type_rune = 4
                    selectRune(1, 9) #Tacle
                else :
                    type_rune = 2
                    selectRune5(1075, 1030)
                    CleanRune()
        elif (A > 425 and A < 431) :
            if G < 7 : 
                indicatif = 6
                type_rune = 6
                selectRune(1, 7) #RePerNeutre
            elif H < 7 : 
                indicatif = 7
                type_rune = 6
                selectRune(1, 8) #RePerEau
            else :
                if I < 20 :
                    indicatif = 8 
                    type_rune = 4
                    selectRune(1, 9) #Tacle
                elif L < 15 :
                    indicatif = 11
                    type_rune = 5
                    selectRune(1, 12)
                elif F < 20:
                    indicatif = 5
                    type_rune = 5 
                    selectRune(1, 6)
                else :
                    type_rune = 2
                    selectRune5(1075, 1030)
                    CleanRune()
        elif A > 430 : 
            if K < 10 :
                indicatif = 9
                type_rune = 7
                selectRune(1, 11) #RePme
            else :
                type_rune = 2
                selectRune5(1075, 1030)
                CleanRune()
        return type_rune, indicatif, False
    #fin étape 2 
    if not G > 6 and (A < 401 and B < 101) :
        indicatif = 6
        type_rune = 6
        selectRune(1, 7) #RePerNeu
        return type_rune, indicatif, False
    if not H > 6 and (A < 401 and B < 101) :
        indicatif = 7
        type_rune = 6
        selectRune(1, 8) #RePerEau
        return type_rune, indicatif, False
    if not K > 8 and (A < 401 and B < 101) :
        indicatif = 9
        if K < 10 :
            type_rune = 7
            selectRune(1, 11) #RetPm
        if K > 10 :
            type_rune = 2
            selectRune5(1075,1030)
            CleanRune()
        return type_rune, indicatif, False
    if not  F > 19 and (A < 401 and B < 101) :
        indicatif = 5
        if F == 17 :
            type_rune = 15
            selectRune(2, 6) #PaDoFeu
        if F == 18 or F == 19 :
            type_rune = 5
            selectRune(1, 6) #DoFeu
        return type_rune, indicatif, False
    if not  I > 18 and (A < 401 and B < 101) :
        indicatif = 8
        if I == 16 :
            type_rune = 12
            selectRune(2, 9) #PaTac
        else:
            type_rune = 4
            selectRune(1, 9) #Tacle
        return type_rune, indicatif, False
    if (A > 389 and B > 91 and C > 25 and D == 4 and F == 20 and G == 7 and H  == 7 and  I > 18 and K > 8 and L == 15) :
        type_rune = 4
        if not I > 19 and type_rune <= poid and (sum(pui) < 694):
            indicatif = 8 
            selectRune(1, 9)
            return type_rune, indicatif, False
        type_rune = 7
        if not K > 9 and type_rune <= poid and (sum(pui) < 694):
            indicatif = 10
            selectRune(1, 11)
            return type_rune, indicatif, False
        type_rune = 9
        if not C > 27 and type_rune <= poid and (sum(pui) < 694):
            indicatif = 2
            selectRune(2, 2)
            return type_rune, indicatif, False
        else :
            type_rune = 6
            if type_rune <= poid : 
                indicatif = 0
                selectRune5(995, 987)
                CleanRune()
                return type_rune, indicatif, False
            elif A > 389 and B > 91 and C > 25 and D == 4 and E == 1 and F == 20 and G == 7 and H == 7 and I > 18 and K > 7 and L == 15 :
                type_rune = 0
                indicatif = 0
                list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                if list_1[0] != '\x0c':
                    if list_1[0].find("% Résistance Feu") != 0 :
                        if list_1[0].find('1') != 0 :
                            indicatif = 0
                            type_rune = 51
                            selectRune5(1122, 985)
                            CleanRune()
                        else :
                            OtherItem(nombre_item)
                        return type_rune, indicatif, False
                    else : 
                        OtherItem(nombre_item)
                        return type_rune, indicatif, False
                else : 
                    indicatif = 0
                    type_rune = 51
                    selectRune5(1122, 985)
                    CleanRune()
                    # OtherItem(nombre_item)
                return type_rune, indicatif, False