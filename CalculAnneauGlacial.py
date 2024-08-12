from pickle import FALSE
from random import *
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
    except IndexError :
        time.sleep(2)
        pyautogui.click(919,582)
        return False, tenta,tenta_plus
    print(A, B, C, D, E, F, G, H)
    ## etape 1  ##
    if not (A > 199 ) and (B < 61 ) :
        if A < 40 or (A > 50 and A < 90) or (A > 100 and A < 140) or (A > 150 and A < 190) :
            selectRune(3,1) #Ra vi
        if (A > 39 and A < 51) or (A > 89 and A < 101) or (A > 139 and A < 151) or (A > 189 and A < 200):
            selectRune(2,1) #Pa vi
        return False, tenta,tenta_plus
    if not B > 46 and (A < 251 and B < 61):  ###1###5### Chance 
        if B == 10 or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) :
            selectRune(3,2) #Ra cha 
        if B < 10 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40) :
            selectRune(2,2) #Pa Cha
        return False, tenta,tenta_plus
    if not C > 31 and (A < 251 and B < 61):  ###2###3### Sagesse
        selectRune(2,3) #Pa Sa
        return False, tenta,tenta_plus
    if not D > 2 and ( A < 251 and B < 61) :
        selectRune(1,4) #Crit
        return False, tenta,tenta_plus
    if not G > 4 and ( A < 251 and B < 61):
        selectRune(2,7) #Pa Fui
        return False, tenta, tenta_plus
    if not H > 12 and (A < 251 and B < 61):
        selectRune(2,8) #Pa re crit
        return False, tenta, tenta_plus
    if not E > 11 and (A< 251 and B < 61) :
        selectRune(2,5) #Pa do Eau
        return False, tenta, tenta_plus
    ## etape 2 ##
    if not (A > 239 and A < 251) and (B < 61):  ###2###9### Vitalité
        if (A > 199 and  A < 206) :
            selectRune(3,1) #Ra Vi
        if (A > 205 and A < 240) :
            selectRune(2,1) #Pa vi
        if (A > 250 and A < 256) :
            if B < 60 :
                selectRune(1,2)
            else:
                selectRune5(1035, 1035) #Ini
        if A > 255 :
            if not H > 19 :
                selectRune(1,8) #Re crit
            else :
                selectRune5(1085, 1030) #Re feu
                CleanRune()
        return False, tenta,tenta_plus
    if not (B > 55 and B < 61)  and (A < 251): 
        if (B > 46 and B < 53) : ###2###8### Chance
            selectRune(3,2) #Ra cha
        if (B > 52 and B < 61):
            selectRune(2,2) #Pa cha
        if B > 60 and B < 62:
            if A < 246 :
                selectRune(1,1)#Vi
            else :
                selectRune5(1035,1034) #Ini
                CleanRune()
        if B > 61 :
            if not H > 19 :
                selectRune(1,8) #Re crit
            else :
                selectRune5(1085, 1030) #Re feu
                CleanRune()
        return False, tenta,tenta_plus
    if not C > 32 and (A < 251 and B < 61):  ###2###3### Sagesse
        selectRune(2,3) #Pa Sa
        return False, tenta,tenta_plus
    if not D > 3 and ( A < 251 and B < 61) :
        selectRune(1,4) #Crit
        return False, tenta,tenta_plus
    if not G > 5 and ( A < 251 and B < 61):
        selectRune(1,7) #Fui
        return False, tenta, tenta_plus
    if not H > 15 and (A < 251 and B < 61):
        if H == 13 or H == 14 :
            selectRune(2,8) #Pa re crit
        else : 
            selectRune(1,8) #Re crit
        return False, tenta, tenta_plus
    if not E > 14 and (A< 251 and B < 61) :
        selectRune(1,5) #do Eau
        return False, tenta, tenta_plus   
    
    if (A > 239 ) and (B > 55 and B < 61) and (C > 32) and (D > 3) and (E > 14) and (G > 5) and (H > 15) :
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
        
