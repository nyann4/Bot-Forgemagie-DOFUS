import time
from Macro1 import * 
from MainScreen import screen
from Reconnect import *

def UpStats2(list_value, poid, nombre_item, tenta, tenta_plus, pui, nom_item, nombre_ligne_item):
  # attribuation des variables en fonction de leur ligne
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
        return type_rune, indicatif, False, tenta, tenta_plus
  # if not (E > 0)  and (A < 251 and B < 61 and C < 61 and H <401 ) and (poid <3): # ligne pour les tenta ++
    if not (E > 0)  and (A < 251 and B < 76) :  ###1###1### Portée
        indicatif = 4
        type_rune = 30
        selectRune(1,5)
        time.sleep(0.4)
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 3
    if not C > 29 and (A < 251 and B < 76): ###1###2### Sagesse
        if C < 25 :
            type_rune = 30 #RaSa
            selectRune(3,3)
        if C > 24 : #PaSa
            type_rune = 9 
            selectRune(2,3)
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 8
    if not I > 9 and (A < 251 and B < 76):  ###1###3### Re crit
        type_rune = 6
        selectRune(2,9) #PaReCri
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 7
    if not H > 2 and (A < 251 and B < 76):  ###1###4### Esquiv Pa
        if H == 0 :
            type_rune = 21 #PaRePA
            selectRune(2,8)
        else :
            type_rune = 7  #RePA
            selectRune(1,8)
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 1
    if not B > 44 and (A < 251 and B < 76):  ###1###5### Age
        if (B > 5 and B < 13 ) or (B > 15 and B < 23 ) or (B > 25 and B < 33 ) or (B > 35 and B < 43) :
            type_rune = 3 #PaAge
            selectRune(2,2)
        else : 
            type_rune = 10
            selectRune(3,2)
        return type_rune, indicatif, False, tenta, tenta_plus
    if not D > 3 and ( A < 251 and B < 76) : #Critique
        type_rune = 10 
        indicatif = 3
        selectRune(1, 4)
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 5
    if not F > 10 and (A < 251 and B < 76):  ###1###6### Dommages Air
        type_rune = 15
        selectRune(2,6)   
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 0
    if not A > 199 and (A < 251 and B < 76):  ###1###8### Vitalité
        if A < 40 or (A > 50 and A < 90) or (A > 100 and A < 140) or (A > 150 and A < 190) :
            type_rune = 3  #PaVi
            selectRune(2,1)
        if (A > 39 and A < 51) or (A > 89 and A < 101) or (A > 139 and A < 151) or (A > 189 and A < 200):
            type_rune = 10 #RaVi
            selectRune(3,1)
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 8
    #FIN ETAPE 1###
    if not I > 13 and (A < 251 and B < 76):  ###2###1### Re crit
        if I == 11 :
            type_rune = 6
            selectRune(2,9)
        else :
            type_rune = 2
            selectRune(1,9)
        return type_rune, indicatif, False, tenta, tenta_plus
    if not  (H > 3 ) and (A < 251 and B < 76):  ###2###2### Esquiv Pa
        type_rune = 7
        indicatif = 7
        selectRune(1, 8)                                
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 2
    if not C > 35 and (A < 251 and B < 76): 
        if C > 30 and C <34 : ###2###3### Sagesse
            type_rune = 30 
            selectRune(2,3)
        else :
            type_rune = 9
            selectRune(2,3)                                
        return type_rune, indicatif, False, tenta, tenta_plus
    if not (B > 69 and B < 76)  and (A < 251): 
        indicatif = 1
        if B > 45 and B < 53 :
            type_rune = 3
            selectRune(2,2)
        elif (B > 52 and B < 76) or B == 45:
            type_rune = 10
            selectRune(3,2)
        elif B > 75:
            if B == 76 :
                if A < 246 :
                    indicatif = 0 
                    type_rune = 1 
                    selectRune(1,1)
                elif I < 15 :
                    indicatif = 8
                    type_rune = 2
                    selectRune(1, 9)
                else : 
                    indicatif = 1
                    type_rune = 1
                    selectRune5(1030, 1045)
                    CleanRune()    
            if B == 77:
                if I < 15 :
                    indicatif = 8
                    type_rune = 2    
                    selectRune(1, 9)
                elif A < 236 :
                    indicatif = 0
                    type_rune = 3
                    selectRune(2,1)
                else : 
                    indicatif = 1
                    type_rune = 2
                    selectRune5(1085, 1030)
                    CleanRune()
            if B == 78:
                if A < 236 :
                    indicatif = 0
                    type_rune = 3
                    selectRune(2,1)
                elif I < 15 :
                    indicatif = 8
                    type_rune = 2    
                    selectRune(1, 9)
                elif C < 45 :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1,3)
                else : 
                    indicatif = 1
                    type_rune = 2
                    selectRune5(1085, 1030)
                    CleanRune()
            if B == 79 :
                if F < 15 :
                    indicatif = 5
                    type_rune = 5
                    selectRune(1, 6)
                elif A < 236 :
                    indicatif = 0
                    type_rune = 3
                    selectRune(2,1)
                elif I < 15 :
                    indicatif = 8
                    type_rune = 2    
                    selectRune(1, 9)
                elif C < 45 :
                    indicatif = 2 
                    type_rune = 3
                    selectRune(1,3)
                else : 
                    indicatif = 1
                    type_rune = 2
                    selectRune5(1085, 1030)
                    CleanRune()
            if B > 79 :
                if F < 15 :
                    indicatif = 5
                    type_rune = 5
                    selectRune(1, 6)
                else : 
                    indicatif = 1
                    type_rune = 2
                    selectRune5(1085, 1030)
                    CleanRune()
        return type_rune, indicatif, False, tenta, tenta_plus  
    indicatif = 0
    if  (A <240 ):  ###2###9### Vitalité
        type_rune = 0
        if (A > 199 and  A < 206) :
            type_rune = 10 #RaVi
            selectRune(3,1)
        if (A > 205 and A < 240) :
            type_rune = 3 # PaVi
            selectRune(2,1)
        return type_rune, indicatif, False, tenta, tenta_plus
    if A > 250 and not (A > 239 and (B > 69 and B < 76) and (C > 35) and (D > 4) and E == 1 and (F > 14 ) and H > 3 and I > 13) :
        if (A > 250 and A < 256):
            if B < 75 :
                indicatif = 1
                type_rune = 1 #Age
                selectRune(1,2)
            else:
                indicatif = 2
                type_rune = 1
                selectRune5(1030, 1045)
                CleanRune()
        if A > 255 :
            if I < 15 :
                indicatif = 8
                type_rune = 2
                selectRune(1, 9)
            else : 
                type_rune = 2
                selectRune5(1085,1034)
                CleanRune()
        return type_rune, indicatif, False, tenta, tenta_plus
    indicatif = 5
    if not D > 4 and (A < 251 and B < 76):  ###2###10### Critique
        if D < 6 :
            type_rune = 10
            indicatif = 3
            selectRune(1,4)
        else : 
            type_rune = 2 
            indicatif = 2
            selectRune5(1085, 1030)
            CleanRune()
        return type_rune, indicatif, False, tenta, tenta_plus           
    indicatif = 8
    if not F > 14 and (A < 251 and B < 76) :
        indicatif = 5
        if F == 11 :
            type_rune = 15
            selectRune(2,6)
        else : 
            type_rune = 5
            selectRune(1,6)
        return type_rune, indicatif, False, tenta, tenta_plus    
    if (A > 239 and A < 301) and (B > 69 and B < 76) and (C > 35) and (D > 4) and E == 1 and (F > 14 ) and H > 3 and I > 13 :
        type_rune = 7
        if not H > 4  and type_rune <= poid: ## Re Pa > 4 
            indicatif = 7
            selectRune(1,8)
            return type_rune, indicatif, False, tenta, tenta_plus
    type_rune = 2
    if not I > 14 and type_rune <= poid :
        indicatif = 8 
        selectRune(1, 9)
        return type_rune, indicatif, False, tenta, tenta_plus
    type_rune = 10
    if not A > 250 and type_rune <= poid :
        indicatif = 0
        selectRune(3,1)
        return type_rune, indicatif, False, tenta, tenta_plus
    type_rune = 3
    if not A > 250 and type_rune <= poid :
        indicatif = 0
        selectRune(2,1)
        return type_rune, indicatif, False, tenta, tenta_plus
    poid = 0
    if (A > 239 and A < 301) and (B > 69 and B < 76) and (C > 35) and (D > 4) and E == 1 and (F > 14 ) and H > 3 and I > 13 :
            if not E > 0 :
                indicatif = 4
                type_rune = 30
                selectRune(1,5)
                return type_rune, indicatif, False, tenta, tenta_plus 
            list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
            if list_1[0].find('PA') != -1 or  list_1[0].find('PM') != -1 or list_1[1].find('PA') != -1 or  list_1[1].find('PM') != -1 :
                type_rune = 100
                print(list_1[0])
                OtherItem(nombre_item)    
                return type_rune, indicatif, False, tenta, tenta_plus                         
            else :
                if list_1[0].find('Initiative') != -1  or list_1[0].find('Feu') != -1 or A > 255:
                    type_rune = 90
                    if sum(pui) >= 455 :
                        tenta_plus += 1
                    tenta += 1
                    suivis_value(list_value, tenta, tenta_plus, pui, nom_item)
                    selectRune5(1166, 1030) #ga pm
                    CleanRune()
                    return type_rune, indicatif, False, tenta, tenta_plus
                else:
                    type_rune = 90
                    if sum(pui) >= 455 :
                        tenta_plus +=1
                    tenta += 1
                    suivis_value(list_value, tenta, tenta_plus, pui, nom_item)
                    selectRune5(1220, 1030) #ga pa
                    CleanRune()
                    return type_rune, indicatif, False, tenta, tenta_plus