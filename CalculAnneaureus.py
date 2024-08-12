from random import *

from pytesseract.pytesseract import cleanup
from Macro1 import * 
from screen import screenValues
from MainScreen import *
import random

def UpStats(list_value, nombre_item, tenta, tenta_plus, nombre_ligne_item):
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
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return False, tenta, tenta_plus
    print(A, B, C, D, E, F, G, H, I, J)
    if not D > 0 and ( A < 401 and B < 71): #crit
        selectRune(1, 4)
        return False, tenta,tenta_plus
    else: 
        if not E > 8 and ( A < 401 and B < 71): #pa do feu
            selectRune(2, 5) #pa do feu
            return False, tenta, tenta_plus
        else : 
            if not B > 49 and ( A < 401 and B < 71):
                if B < 8 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40 and B < 48) : #PaIne
                    selectRune(2, 2)  
                if (B > 7 and B < 11) or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) or (B > 47 and B < 50) :#RaIne
                    selectRune(3, 2)
                return False, tenta, tenta_plus
            else : 
                if not (A > 179 ) and ( A < 401 and B < 71):
                    if (A == 0 )  or ( A > 39 and A < 51 ) or ( A > 89 and A < 101) or (A > 139 and A < 151) :
                        selectRune(3, 1) # ravi
                    else :
                        selectRune(2, 1) # pa vi
                    return False, tenta, tenta_plus
                else :
                    if not C > 25 and ( A < 401 and B < 71): # Pa Sa
                        selectRune(2, 3)
                        return False, tenta, tenta_plus
                    else:
                        if not F > 6 and ( A < 401 and B < 71): #Pa SO
                            selectRune(2, 6)
                            return False, tenta, tenta_plus
                        else : 
                            if not H > 4 and ( A < 401 and B < 71): #Re Per terre
                                selectRune(1, 8)
                                return False, tenta, tenta_plus
                            else :
                                if not I > 4 and ( A < 401 and B < 71): #Re per eau
                                    selectRune(1, 9)
                                    return False, tenta, tenta_plus
                                else : 
                                    if not J > 6 and ( A < 401 and B < 71): #Pa Re Pa
                                        selectRune(2, 10)
                                        return False, tenta, tenta_plus
                                        #fin étape 1
                                    else : 
                                        if (not (B > 65 and B < 71)) and A < 401 :
                                            if B == 50 or (B > 57  and B < 66):
                                                selectRune(3, 2) #RaIne
                                            elif B > 50 and B < 58 :
                                                selectRune(2, 2) #PaIne
                                            elif B > 70 :
                                                if B == 71 :
                                                    if A < 346 :
                                                        selectRune(1, 1) #Vi
                                                    else :
                                                        selectRune5(1045, 1030) #Ini
                                                        CleanRune()
                                                if B == 72 :
                                                    if A < 336 :
                                                        selectRune(2, 1) #PaVi
                                                    else : 
                                                        selectRune5(1085, 1030) #ReFeu
                                                        CleanRune()
                                                if B == 73 :
                                                    if A < 336 :
                                                        selectRune(2, 1) #PaVi
                                                    elif C < 40 :
                                                        selectRune(1, 3) #Sa
                                                    else : 
                                                        selectRune5(1085, 1030) #ReFeu
                                                        CleanRune()
                                                if B == 74 :
                                                    if C < 40 :
                                                        selectRune(1, 3) #Sa
                                                    elif A < 336 :
                                                        selectRune(2, 1) #PaVi
                                                    elif E < 12 :
                                                        selectRune(1, 5) #Do feu
                                                    else : 
                                                        selectRune5(1085, 1030) #ReFeu
                                                        CleanRune()
                                                if B > 74 :
                                                    if E < 12 :
                                                        selectRune(1, 5) #Do Feu
                                                    elif C < 40 :
                                                        selectRune(1, 3) #Sa
                                                    elif A < 336 :
                                                        selectRune(2, 1) #PaVi
                                                    else : 
                                                        selectRune5(1085, 1030) #ReFeu
                                                        CleanRune()
                                            return False, tenta, tenta_plus
                                        else : 
                                            if not C > 32 and ( A < 401 and B < 71):
                                                selectRune(2, 3) # PaSa
                                                return False, tenta, tenta_plus
                                            else : 
                                                if not D > 1 and D < 3 and ( A < 401 and B < 71):
                                                    if D < 3 :
                                                        selectRune(1, 4) # Crit
                                                    if D > 2 :
                                                        if F < 12 :
                                                            selectRune(1, 6) #Do Terre
                                                        elif E < 12 :
                                                            selectRune(1, 5) #Do Neutre
                                                        elif C < 38 :
                                                            selectRune(2, 3) #PaSa
                                                        else : 
                                                            selectRune5(1085, 1030) #ReFeu
                                                            CleanRune()
                                                    return False, tenta, tenta_plus
                                                else : 
                                                    if not J > 7 and ( A < 401 and B < 71):
                                                        selectRune(1, 10) # Re Pa
                                                        return False, tenta, tenta_plus
                                                    else : 
                                                        if not (A > 389 and A < 401) and B < 71 : 
                                                            if (A > 189 and A < 201) or (A > 239 and A < 251) or (A > 289 and A < 390):
                                                                selectRune(3, 1) #RaVi
                                                            elif  (A > 150 and A < 190) or (A > 200 and A < 240) or (A > 250 and A < 290) :
                                                                selectRune(2, 1) #PaVi
                                                            elif A > 400 :
                                                                if A < 406 :
                                                                    if B < 70 :
                                                                        selectRune(1, 2) #Ine
                                                                    else :
                                                                        selectRune5(1045, 1030) #Ini
                                                                        CleanRune()
                                                                if A > 405 and A < 411:
                                                                    selectRune5(1085, 1030)
                                                                    CleanRune()
                                                                if A > 410 and A < 416:
                                                                    if B < 68 :
                                                                        selectRune(2, 2) #PaIne
                                                                    elif C < 40 :
                                                                        selectRune(1, 3) #Sa
                                                                    else : 
                                                                        selectRune5(1085, 1030) #ReFeu
                                                                        CleanRune()
                                                                if A > 415 and A < 421 :
                                                                    if C < 40 :
                                                                        selectRune(1, 3) #Sa
                                                                    elif B < 68 :
                                                                        selectRune(2, 2) #PaIne
                                                                    elif E < 12 :
                                                                        selectRune(1, 5) #Do Feu
                                                                    else : 
                                                                        selectRune5(1085, 1030) #ReFeu
                                                                        CleanRune()
                                                                if  A > 420 and A < 426 :
                                                                    if E < 12 :
                                                                            selectRune(1, 5) #Do Feu
                                                                    elif B < 68 :
                                                                            selectRune(2, 2) #PaIne
                                                                    elif C < 40 :
                                                                            selectRune(1, 3) #Sa
                                                                    else : 
                                                                        selectRune5(1085, 1030) #ReFeu
                                                                        CleanRune()
                                                                if A > 425 :
                                                                    if I < 7 :
                                                                        selectRune(1, 9) #re per eau
                                                                    elif E < 12 :
                                                                            selectRune(1, 5) #Do Feu
                                                                    elif H < 7 :
                                                                            selectRune(1, 8) #Re per terre
                                                                    elif B < 68 :
                                                                            selectRune(2, 2) #PaFo
                                                                    elif C < 40 :
                                                                            selectRune(1, 3) #Sa
                                                                    else : 
                                                                        selectRune5(1085, 1030) #ReFeu
                                                                        CleanRune()                                
                                                            return False, tenta, tenta_plus
                                                        else : 
                                                            if not I > 6 and I < 8 and ( A < 401 and B < 71):
                                                                if I < 8 :
                                                                    selectRune(1, 9) #Re Per Eau
                                                                if I > 7 :
                                                                    if E < 12 :
                                                                        selectRune(1, 5) #Do Feu
                                                                    elif C < 38 :
                                                                        selectRune(1, 3) #PaSa
                                                                    else : 
                                                                        selectRune5(1085, 1030) #ReFeu
                                                                        CleanRune()
                                                                return False, tenta, tenta_plus
                                                            else : 
                                                                if not H > 6 and H < 8 and ( A < 401 and B < 71):
                                                                    if H < 8 :
                                                                        selectRune(1, 8) #Re Per Terre
                                                                    if H > 7 :
                                                                        if E < 12 :
                                                                            selectRune(1, 5) #Do Feu
                                                                        elif C < 38 :
                                                                            selectRune(1, 3) #Sa
                                                                        else : 
                                                                            selectRune5(1085, 1030) #ReFeu
                                                                            CleanRune()
                                                                    return False, tenta, tenta_plus
                                                                else : 
                                                                    if not E > 10 and ( A < 401 and B < 71):
                                                                        if E == 8 :
                                                                            selectRune(2, 5) #Pa Do Feu
                                                                        if E == 9 or E == 10 :
                                                                            selectRune(1, 5) #Do Feu
                                                                        return False, tenta, tenta_plus
                                                                    else :
                                                                        if not F > 7 and ( A < 401 and B < 71):
                                                                            selectRune(1, 6) #So
                                                                            return False, tenta, tenta_plus
                                                                        else : 
                                                                            if not E > 11 and (A < 401 and B < 71) :
                                                                                selectRune(1, 5) #do feu
                                                                                return False, tenta, tenta_plus
                                                                            else :
                                                                                if (A > 389 ) and (B > 65 and B < 71) and (C > 32) and (D > 1) and (E > 11) and (F > 7) and (H > 6) and (I > 6) and (J > 7):
                                                                                    list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                                    if list_1[0] != '\x0c' :
                                                                                        if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                                                                                            OtherItem(nombre_item) 
                                                                                        else:
                                                                                            selectRune5(1166, 1030) # PM
                                                                                            CleanRune()
                                                                                            tenta +=1          
                                                                                            return False, tenta, tenta_plus         
                                                                                    else :
                                                                                        time.sleep(0.15)
                                                                                        selectRune5(1212, 1030) # Ga Pa
                                                                                        tenta +=1 
                                                                                        CleanRune()
                                                                                        time.sleep(0.25)
                                                                                        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                                        if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                                                                                            OtherItem(nombre_item)    
                                                                                    return False, tenta, tenta_plus 