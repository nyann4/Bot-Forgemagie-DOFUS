from distutils.command.clean import clean
import time
from MainScreen import *
import re
from Macro1 import * 
from screen import *

def UpStats2(list_value, poid, nombre_item,nombre_ligne_item, tenta, max_rune1, max_rune2, max_rune3):
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
        J = int(list_value[9])
        K = int(list_value[10])
        L = int(list_value[11])
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return type_rune, indicatif, False, tenta
    list_value = screenValues(853, 487, 200, 40, 1 )
    if list_value[0].find('rror') != -1  or list_value[0].find('Attention') != -1:
        time.sleep(2)
        pyautogui.click(919,582)
        return type_rune, indicatif, False, tenta

    if not (E > 0)  and (A < max_rune1 and B < max_rune2 and I< max_rune3) and (poid <6):
        time.sleep(0.2)
        indicatif = 4
        type_rune = 51
        selectRune(1,5) # Po
        return type_rune, indicatif, False, tenta
    if not D > 0  and (A < max_rune1 and B < max_rune2 and I< max_rune3) and (poid <6):
        time.sleep(0.2)
        indicatif = 3
        type_rune = 10
        selectRune(1, 4) #Pa
        return type_rune, indicatif, False, tenta
    if not (J > 4 ) and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 9
        type_rune = 6
        selectRune(1, 10) #RePerNeu
        return type_rune, indicatif, False, tenta
    if not C > 29 and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 2
        type_rune = 9
        selectRune(2, 3) #PaSa
        return type_rune, indicatif, False, tenta 
    if not (K > 5) and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 10
        type_rune = 6
        selectRune(1, 11)  #RePerAir
        return type_rune, indicatif, False, tenta
    if not (A > 289)  and (B < max_rune2) :
        indicatif = 0
        if A == 0 or (A > 0 and A < 266) :
            type_rune = 10
            selectRune(3, 1) #RaVi
        if (A > 265 and A < 290) :
            type_rune = 3
            selectRune(2, 1) #PaVi
        return type_rune, indicatif, False, tenta
    if not (G > 8) and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 6
        type_rune = 15
        selectRune(2, 7) #PaDoTerre
        return type_rune, indicatif, False, tenta
    if not (F > 8) and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 5
        type_rune = 15
        selectRune(2, 6) #PaDoNeutre
        return type_rune, indicatif, False, tenta
    if not (H > 12) and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 7
        type_rune = 30
        selectRune(2, 8) #PaSoin
        return type_rune, indicatif, False, tenta
    if not B > 59 and (A < max_rune1) and (I < max_rune3) :
        indicatif = 1
        if (B < 8) or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40 and B < 48 ) or (B > 50 and B < 58) :
            type_rune = 3
            selectRune(2, 2) #PaFo
        else :
            type_rune = 10
            selectRune(3, 2) #RaFo
        return type_rune, indicatif, False, tenta
    if not I > 399 and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 8
        if (I < 71) or (I > 100 and I < 171) or (I > 200 and I < 271) or (I > 300 and I < 371) :
            type_rune = 3
            selectRune(2, 9) #PaIni
        elif (I > 379 and I < 390) or (I > 279 and I < 290) or (I > 179 and I < 190) or (I > 79 and I < 90):
            type_rune = 1 
            selectRune(1,9)
        else :
            type_rune = 10
            selectRune(3, 9) #RaIni
        return type_rune, indicatif, False, tenta
    if not L > 4 and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 11
        type_rune = 21
        selectRune(2, 12) #PaRePa
        return type_rune, indicatif, False, tenta
    #Fin étape 1 
    if not (H > 16) and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 7
        if H < 16 :
            type_rune = 30
            selectRune(2, 8) #PaSoin
        if H == 16:
            type_rune = 10
            selectRune(1, 8) #Soin
        return type_rune, indicatif, False, tenta
    if not (C > 35) and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 2
        type_rune = 9
        selectRune(2, 3) #PaSa
        return type_rune, indicatif, False, tenta
    if not (L > 6) and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 11
        type_rune = 7
        selectRune(1, 12) #RePa
        return type_rune, indicatif, False, tenta
    if not C > 6 and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 9
        type_rune = 6
        selectRune(1, 10) #RePerNeutre
        return type_rune, indicatif, False, tenta
    if not (B > 66 and B < max_rune2) and (A < max_rune1 and I < max_rune3) :
        indicatif = 1
        if B < 66 :
            type_rune = 10
            selectRune(3,2)
        if B > 65 and B < 71:
            type_rune = 3
            selectRune(2, 2)
        if B > max_rune2-1:
            if B == max_rune2:
                if I < 491 :
                    type_rune = 1
                    indicatif = 8
                    selectRune(1, 9) #Ini
                elif A < 396 :
                    type_rune = 1 
                    indicatif = 1
                    selectRune(1, 1) #Vi
                else :
                    type_rune = 1
                    selectRune5(996, 989) #rune ine
                    CleanRune()
            if B == (max_rune2 +1):
                type_rune = 2
                selectRune5(1075, 1030) # Refeu
                CleanRune()
            if B == (max_rune2+2):
                if I < 471:
                    indicatif = 8
                    type_rune = 3
                    selectRune(2, 9) #PaIni
                else :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1,3) #Sa
            if B == (max_rune2+3):
                if I < 471:
                    indicatif = 8
                    type_rune = 3
                    selectRune(2, 9) #PaIni
                else :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1,3) #Sa
            if B == (max_rune2+4):
                if F < 12 :
                    indicatif = 5
                    type_rune = 5
                    selectRune(1,6) #do neutre
                elif G < 12 :
                    indicatif = 6
                    type_rune = 5
                    selectRune(1, 7) #do terre
                elif I < 471:
                    indicatif = 8
                    type_rune = 3
                    selectRune(2, 9) #PaIni
                else :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1,3) #Sa
            if B == (max_rune2+5):
                if J < 7 :
                    indicatif = 9
                    type_rune = 6
                    selectRune(1, 10) #RePerNeutre
                if K < 7 :
                    indicatif = 10
                    type_rune = 6
                    selectRune(1, 11) #RePerAir
                elif I < 471:
                    indicatif = 8
                    type_rune = 3
                    selectRune(2, 9) #PaIni
                else :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1,3) #Sa
            if B ==(max_rune2+6):
                if L < 8 :
                    indicatif = 11
                    type_rune = 7
                    selectRune(1, 12) #Repa
                else :
                    indicatif = 2
                    type_rune = 3
                    selectRune(1, 3) #Sa
        return type_rune, indicatif, False, tenta
    if not (A > 389 and A < 401)  and (B < max_rune2) : 
        indicatif =  1
        if (A > 289 and A < 311 ) or (A > 339 and A < 390) :
            type_rune = 10
            selectRune(3, 1) #RaVi
        elif (A > 310 and A < 340) :
            type_rune = 3
            selectRune(2, 1) #PaVi
        elif A > 400 and A < 406 :
            if I < 491 :
                indicatif = 8
                type_rune = 1
                selectRune(1, 9) #Ini
            else :
                type_rune = 1
                selectRune5(996, 989) #Ine
                CleanRune() 
        elif A > 405 and A < 411 :
            type_rune = 1
            selectRune5(1075, 1030) #Refeu
            CleanRune()
        elif (A > 410 and A < 416 ) :
            if  C < 40:
                indicatif = 2
                type_rune = 3
                selectRune(1, 3) #Sa
            else : 
                type_rune = 2
                selectRune5(1075, 1030)
                CleanRune()
        elif (A > 415 and A < 421):
            indicatif = 2
            type_rune = 3
            selectRune(1, 3) #Sa
        elif (A > 420 and A < 426):
            if F < 12 :
                indicatif = 5
                type_rune = 5
                selectRune(1, 6) #DoNeutre                                        
            elif G < 12 :
                indicatif = 6
                type_rune = 5
                selectRune(1, 7) #DoTerre
            else : 
                type_rune = 2
                selectRune5(1075, 1030) #Refeu
                CleanRune()
        elif (A > 425 and A < 431) :
            if J < 7 : 
                indicatif = 9
                type_rune = 6
                selectRune(1, 10) #RePerNeutre
            elif K < 7 : 
                indicatif = 10
                type_rune = 6
                selectRune(1, 11) #RePerAir
            else :
                type_rune = 1
                selectRune5(996, 989) #ine
                CleanRune()
        elif A > 430 : 
            if L < 8 :
                indicatif = 11
                type_rune = 7
                selectRune(1, 12) #RePa
            else :
                type_rune = 2
                selectRune5(1075, 1030)
                CleanRune()
        return type_rune, indicatif, False, tenta
    if not G > 11 and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 6
        type_rune = 5
        selectRune(1, 7) #DoTerre
        return type_rune, indicatif, False, tenta
    if not (I > 489 and I < 501) and (A < max_rune1 and B < max_rune2) :
        indicatif = 8
        if I < 501:
            if I > 379 and I < 390 :
                type_rune = 1
                selectRune(1, 9)
            if (I > 410 and I < 430) :
                type_rune = 10
                selectRune(3, 9) #RaIni
            else :
                type_rune = 3
                selectRune(2, 9) #PaIni
        else : 
            if I > 500:
                if I > 500 and I < 511:
                    type_rune = 1
                    selectRune5(996, 989) #Rune ine
                    CleanRune()
                if I > 510 and I < 521 :
                    type_rune = 2
                    selectRune5(1075, 1030) #Refeu
                    CleanRune()
                if I > 520 :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1, 3) #Sa
        return type_rune, indicatif, False, tenta
    if not F > 11 and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 5
        type_rune = 5
        selectRune(1, 6) #DoNeutre
        return type_rune, indicatif, False, tenta
    if not K > 6 and (A < max_rune1 and B < max_rune2 and I< max_rune3) :
        indicatif = 10
        type_rune = 6
        selectRune(1, 11) #RePerAir
        return type_rune, indicatif, False, tenta
    if not J > 6 and (A < max_rune1 and B < max_rune2 and I< max_rune3) and I < 501 :
        indicatif = 9
        type_rune = 6
        selectRune(1, 10) #RePerNeutre
        return type_rune, indicatif, False, tenta
    if A > 389 and B > 66 and C > 35 and F == 12 and G == 12 and H > 16 and I > 489 and J == 7 and K == 7 and L > 7 and (D == 0 or E == 0):
        type_rune = 6
        indicatif = 1
        if type_rune <= poid :
            selectRune5(953, 1030) #RePerTerre
            CleanRune()
            return type_rune, indicatif, False, tenta
    if not (L > 7) and (A < max_rune1 and B < max_rune2 and I< max_rune3):
        indicatif = 11
        type_rune = 7
        selectRune(1, 12) #RePa
        return type_rune, indicatif, False, tenta
    if A > 389 and B > 66 and C > 35 and D == 1 and E == 1 and F == 12 and G == 12 and H > 16 and I > 489 and J == 7 and K == 7 and L > 7 and poid < 6 :
        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
        print('exo' , list_1[0])
        list_1[0] = re.sub("[^0-9]","", list_1[0]) 
        print('exo' , list_1[0])
        if list_1[0] == '1' or list_1[0] == '':
            indicatif = 0
            type_rune = 90
            selectRune5(1176, 1032) #Pm
            CleanRune()
            return type_rune,indicatif, False, tenta
        else :
            OtherItem(nombre_item)
            type_rune = 1
            indicatif = 4
            return type_rune,indicatif, False, tenta