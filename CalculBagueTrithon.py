import time
from Macro1 import * 
from screen import *
from Conditions import *

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
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return False, tenta, tenta_plus
    print(A, B, C, D, E, F, G, H, I)
    if not D > 4 and ( A < 401): #RePerTerre
        selectRune(1, 4)
        return False, tenta,tenta_plus
    else: 
        if not E > 4 and ( A < 401): # RePerEau
            selectRune(1, 5)
            return False, tenta, tenta_plus
        else : 
            if not B > 25 and ( A < 401):
                selectRune(2, 2)  
                return False, tenta, tenta_plus
            else : 
                if not (A > 240 ) :
                    if (A == 0 ) or (A > 0 and A < 101) or (A > 144 and A < 165) or (A > 189 and A < 201) or A == 240:
                        selectRune(3, 1) # ravi
                    if (A > 100 and A < 145) or (A > 164 and A < 190) or (A > 200 and A < 240) :
                        selectRune(2, 1) # pa vi
                    return False, tenta, tenta_plus
                else :
                        if not F > 5 and ( A < 401): #Pa Tacle
                            selectRune(2, 6)
                            return False, tenta, tenta_plus
                        else : 
                            if not H > 12 and ( A < 401): #Pa Do Crit
                                selectRune(2, 8)
                                return False, tenta, tenta_plus
                            else :
                                if not G > 4 and ( A < 401): #Esquiv Pa
                                    selectRune(2, 7)
                                    return False, tenta, tenta_plus
                                else : 
                                    if not I > 10 and ( A < 401): #Pa Do pou
                                        selectRune(2, 9)
                                        return False, tenta, tenta_plus
                                        #fin étape 1
                                    else : 
                                        if not B > 30 and A < 401 :
                                            selectRune(2,2)
                                            return False, tenta, tenta_plus
                                        else : 
                                                if not D > 6 and D < 8 and ( A < 401):
                                                    if D < 8 :
                                                        selectRune(1, 4) # Crit
                                                    if D > 7 :
                                                        if H < 20:
                                                            selectRune(1, 8)
                                                        elif I < 15 :
                                                            selectRune(1, 9)
                                                        else : 
                                                            selectRune5(1085, 1030) #ReFeu
                                                            CleanRune()
                                                    return False, tenta, tenta_plus
                                                else : 
                                                    if not G > 7 and ( A < 401):
                                                        selectRune(1, 7) # Esquiv Pa
                                                        return False, tenta, tenta_plus
                                                    else : 
                                                        if not (A > 389 and A < 401): 
                                                            if (A > 240 and A < 261) or (A > 289 and A < 311 ) or (A > 339 and A < 390) :
                                                                selectRune(3, 1) #RaVi
                                                            elif (A > 260 and A < 290 ) or (A > 310 and A < 340) :
                                                                selectRune(2, 1) #PaVi
                                                            elif A > 400 and A < 406 :
                                                                selectRune5(1030, 1030)
                                                                CleanRune() 
                                                            elif A > 405 and A < 411 :
                                                                selectRune5(1075, 1030)
                                                                CleanRune()
                                                            elif (A > 410 and A < 416 ) :
                                                                if  B < 40:
                                                                    selectRune(1, 2) #Sa
                                                                else : 
                                                                    selectRune5(1075, 1030)
                                                                    CleanRune()
                                                            elif (A > 415 and A < 421):
                                                                if F < 10:
                                                                    selectRune(1, 6)
                                                                else:
                                                                    selectRune5(1075, 1030)
                                                                    CleanRune()
                                                            elif (A > 420 and A < 426):
                                                                if H < 20 :
                                                                    selectRune(1, 8) #DoCrit                                         
                                                                elif I < 15 :
                                                                    selectRune(1, 9) #DoFeu
                                                                else : 
                                                                    selectRune5(1075, 1030)
                                                                    CleanRune()
                                                            elif (A > 425 and A < 431) :
                                                                if D < 7 : 
                                                                    selectRune(1, 4) #RePerFeu
                                                                elif E < 7:
                                                                    selectRune(1, 5)
                                                                else :
                                                                    selectRune5(1030, 1030)
                                                                    CleanRune()
                                                            elif A > 430 : 
                                                                if G < 10 :
                                                                    selectRune(1, 7) #RePA
                                                                else :
                                                                    selectRune5(1075, 1030)
                                                                    CleanRune()
                                                            return False, tenta, tenta_plus
                                                        else : 
                                                            if not I > 13 and ( A < 401 and B < 81):
                                                                selectRune(1, 9) # Do Pou
                                                                return False, tenta, tenta_plus
                                                            else : 
                                                                if not F > 7  and ( A < 401 and B < 81): #Tacle
                                                                    selectRune(1, 6) #Tacle
                                                                    return False, tenta, tenta_plus
                                                                else : 
                                                                    if not E > 6 and E < 8 and ( A < 401):
                                                                        if E < 7 :
                                                                            selectRune(1, 5)
                                                                        if E > 7 :
                                                                            if H < 20:
                                                                                selectRune(1, 8)
                                                                            elif I < 15 :
                                                                                selectRune(1, 9)
                                                                            else : 
                                                                                selectRune5(1085, 1030) #ReFeu
                                                                                CleanRune()
                                                                        return False, tenta, tenta_plus
                                                                    else :
                                                                        if not H > 18 and ( A < 401):
                                                                            if H == 16 or H == 13 :
                                                                                selectRune(2, 8)
                                                                            else : 
                                                                                selectRune(1, 8) #Do Crit
                                                                            return False, tenta, tenta_plus
                                                                        else :
                                                                            if (A > 389 ) and (B > 30)  and (D > 6) and (E > 6) and (F > 7) and (G > 7) and (H > 18) and (I > 13):
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

