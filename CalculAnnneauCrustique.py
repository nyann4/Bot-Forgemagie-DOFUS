from random import *
from pytesseract.pytesseract import cleanup
from Macro1 import * 
from screen import screenValues
from MainScreen import *
import json

def UpStats(list_value, nombre_item, tenta, tenta_plus, nombre_ligne_item, nom_item):
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
    path = "C:\\Users\\yannf\\OneDrive\\SWSetup\\Bureau\\PROJET0\\CODE\\all_codes\\DictionnaireItem\\item.json"
    with open(path, encoding='utf-8') as outfile:
        data =json.load(outfile)
    print(A, B, C, D, E, F, G, H, I)
    if not D > 0 and ( A < 351 and B < 81): #crit
        type_rune, indicatif = selectRune(1,4, data, nom_item)
        return False, tenta,tenta_plus
    else: 
        if not E > 7 and ( A < 351 and B < 81): # Pa do neutre
            type_rune, indicatif = selectRune(2,5, data, nom_item)
            return False, tenta, tenta_plus
        else : 
            if not B > 49 and ( A < 351 and B < 81):
                if B < 8 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40 and B < 48) : #PaFo
                    type_rune, indicatif = selectRune(2,2, data, nom_item)  
                if (B > 7 and B < 11) or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) or (B > 47 and B < 50) :#RaFo
                    type_rune, indicatif = selectRune(3,2, data, nom_item)
                return False, tenta, tenta_plus
            else : 
                if not (A > 179 ) and ( A < 351 and B < 81):
                    if (A == 0 ) or (A > 0 and A < 101) or (A > 144 and A < 165) :
                        type_rune, indicatif = selectRune(3,1, data, nom_item) # ravi
                    if (A > 100 and A < 145) or (A > 164 and A < 180) :
                        type_rune, indicatif = selectRune(2,1, data, nom_item) # pa vi
                    return False, tenta, tenta_plus
                else :
                    if not C > 25 and ( A < 351 and B < 81): # Pa Sa
                        type_rune, indicatif = selectRune(2,3, data, nom_item)
                        return False, tenta, tenta_plus
                    else:
                        if not F > 7 and ( A < 351 and B < 81): #Pa Do Terre
                            type_rune, indicatif = selectRune(2,6, data, nom_item)
                            return False, tenta, tenta_plus
                        else : 
                            if not G > 4 and ( A < 351 and B < 81): #Re Per Eau
                                type_rune, indicatif = selectRune(1,7, data, nom_item)
                                return False, tenta, tenta_plus
                            else :
                                if not H > 6 and ( A < 351 and B < 81): #Pa Tacle
                                    type_rune, indicatif = selectRune(2,8, data, nom_item)
                                    return False, tenta, tenta_plus
                                else : 
                                    if not I > 6 and ( A < 351 and B < 81): #Pa Retrait Pa
                                        type_rune, indicatif = selectRune(2,9, data, nom_item)
                                        return False, tenta, tenta_plus
                                        #fin étape 1
                                    else : 
                                        if (not (B > 75 and B < 81)) and A < 351 :
                                            if B == 50 or (B > 59  and B < 76):
                                                type_rune, indicatif = selectRune(3,2, data, nom_item) #RaFo
                                            elif B > 50 and B < 60 :
                                                type_rune, indicatif = selectRune(2,2, data, nom_item) #PaFo
                                            elif B > 80 :
                                                if B == 81 :
                                                    if A < 346 :
                                                        type_rune, indicatif = selectRune(1,1, data, nom_item) #Vi
                                                    else :
                                                        type_rune, indicatif = selectRune5('ini') #Ini
                                                        CleanRune()
                                                if B == 82 :
                                                    if A < 336 :
                                                        type_rune, indicatif = selectRune(2,1, data, nom_item) #PaVi
                                                    else : 
                                                        type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                        CleanRune()
                                                if B == 83 :
                                                    if A < 336 :
                                                        type_rune, indicatif = selectRune(2,1, data, nom_item) #PaVi
                                                    elif C < 40 :
                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                    elif H < 10 :
                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                    else : 
                                                        type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                        CleanRune()
                                                if B == 84 :
                                                    if H < 10 :
                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                    elif C < 40 :
                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                    elif A < 336 :
                                                        type_rune, indicatif = selectRune(2,1, data, nom_item) #PaVi
                                                    elif E < 12 :
                                                        type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                    elif F < 12 :
                                                        type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                    else : 
                                                        type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                        CleanRune()
                                                if B > 84 :
                                                    if E < 12 :
                                                        type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                    elif F < 12 :
                                                        type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                    elif H < 10 :
                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                    elif C < 40 :
                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                    elif A < 336 :
                                                        type_rune, indicatif = selectRune(2,1, data, nom_item) #PaVi
                                                    else : 
                                                        type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                        CleanRune()
                                            return False, tenta, tenta_plus
                                        else : 
                                            if not C > 32 and ( A < 351 and B < 81):
                                                type_rune, indicatif = selectRune(2,3, data, nom_item) # PaSa
                                                return False, tenta, tenta_plus
                                            else : 
                                                if not D > 1 and D < 3 and ( A < 351 and B < 81):
                                                    if D < 3 :
                                                        type_rune, indicatif = selectRune(1,4, data, nom_item) # Crit
                                                    if D > 2 :
                                                        if F < 12 :
                                                            type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                        elif E < 12 :
                                                            type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                        elif C < 38 :
                                                            type_rune, indicatif = selectRune(2,3, data, nom_item) #PaSa
                                                        else : 
                                                            type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                            CleanRune()
                                                    return False, tenta, tenta_plus
                                                else : 
                                                    if not H > 7 and ( A < 351 and B < 81):
                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) # Tacle
                                                        return False, tenta, tenta_plus
                                                    else : 
                                                        if not (A > 339 and A < 351) and B < 81 : 
                                                            if (A < 101) or (A > 139 and A < 169) or (A > 194 and A < 210) or (A > 239 and A < 266) or (A > 289 and A < 340):
                                                                type_rune, indicatif = selectRune(3,1, data, nom_item) #RaVi
                                                            elif (A > 100 and A < 140) or (A > 168 and A < 195) or (A > 209 and A < 240) or (A > 265 and A < 290) :
                                                                type_rune, indicatif = selectRune(2,1, data, nom_item) #PaVi
                                                            elif A > 350 :
                                                                if A < 356 :
                                                                    if B < 80 :
                                                                        type_rune, indicatif = selectRune(1,2, data, nom_item) #Fo
                                                                    else :
                                                                        type_rune, indicatif = selectRune5('ini') #Ini
                                                                        CleanRune()
                                                                if A > 355 and A < 361:
                                                                    type_rune, indicatif = selectRune5('refeu')
                                                                    CleanRune()
                                                                if A > 360 and A < 366:
                                                                    if B < 78 :
                                                                        type_rune, indicatif = selectRune(2,2, data, nom_item) #PaFo
                                                                    elif C < 40 :
                                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                                    elif H < 10 :
                                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                                    else : 
                                                                        type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                                        CleanRune()
                                                                if A > 365 and A < 371 :
                                                                    if H < 10 :
                                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                                    elif C < 40 :
                                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                                    elif B < 78 :
                                                                        type_rune, indicatif = selectRune(2,2, data, nom_item) #PaFo
                                                                    elif E < 12 :
                                                                        type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                                    elif F < 12 :
                                                                        type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                                    else : 
                                                                        type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                                        CleanRune()
                                                            if  A > 370 and A < 376 :
                                                                if E < 12 :
                                                                        type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                                elif F < 12 :
                                                                    selectRune4(1083, 556) #Do Terre
                                                                elif H < 10 :
                                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                                elif B < 78 :
                                                                        type_rune, indicatif = selectRune(2,2, data, nom_item) #PaFo
                                                                elif C < 40 :
                                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                                else : 
                                                                    type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                                    CleanRune()
                                                            if A > 375 :
                                                                if G < 7 :
                                                                    type_rune, indicatif = selectRune(1,7, data, nom_item) #re per eau
                                                                elif E < 12 :
                                                                        type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                                elif F < 12 :
                                                                    type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                                elif H < 10 :
                                                                        type_rune, indicatif = selectRune(1,8, data, nom_item) #Tacle
                                                                elif B < 78 :
                                                                        type_rune, indicatif = selectRune(2,2, data, nom_item) #PaFo
                                                                elif C < 40 :
                                                                        type_rune, indicatif = selectRune(1,3, data, nom_item) #Sa
                                                                else : 
                                                                    type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                                    CleanRune()                                
                                                            return False, tenta, tenta_plus
                                                        else : 
                                                            if not I > 7 and ( A < 351 and B < 81):
                                                                type_rune, indicatif = selectRune(1,9, data, nom_item) # Ret Pa
                                                                return False, tenta, tenta_plus
                                                            else : 
                                                                if not G > 6 and G < 8 and ( A < 351 and B < 81):
                                                                    if G < 8 :
                                                                        type_rune, indicatif = selectRune(1,7, data, nom_item) #Re Per Eau 
                                                                    if G > 7 :
                                                                        if F < 12 :
                                                                            type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                                        elif E < 12 :
                                                                            type_rune, indicatif = selectRune(1,5, data, nom_item) #Do Neutre
                                                                        elif C < 38 :
                                                                            type_rune, indicatif = selectRune(1,3, data, nom_item) #PaSa
                                                                        else : 
                                                                            type_rune, indicatif = selectRune5('refeu') #ReFeu
                                                                            CleanRune()
                                                                    return False, tenta, tenta_plus
                                                                else : 
                                                                    if not E > 10 and ( A < 351 and B < 81):
                                                                        if E == 8 :
                                                                            type_rune, indicatif = selectRune(2,5, data, nom_item) #Pa Do neutre
                                                                        if E == 9 or E == 10 :
                                                                            type_rune, indicatif = selectRune(1,5, data, nom_item) #Do neutre
                                                                        return False, tenta, tenta_plus
                                                                    else :
                                                                        if not F > 10 and ( A < 351 and B < 81):
                                                                            if F == 8 :
                                                                                type_rune, indicatif = selectRune(2,6, data, nom_item) #Pa Do Terre
                                                                            if F == 9 or F == 10 :
                                                                                type_rune, indicatif = selectRune(1,6, data, nom_item) #Do Terre
                                                                            return False, tenta, tenta_plus
                                                                        else :
                                                                            if (A > 339 ) and (B > 75 and B < 81) and (C > 32) and (D > 1) and (E > 10) and (F > 10) and (G > 6) and (H > 7) and (I > 7):
                                                                                list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                                if list_1[0] != '\x0c' :
                                                                                    if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                                                                                        OtherItem(nombre_item) 
                                                                                    else:
                                                                                        type_rune, indicatif = selectRune5('pm') # PM
                                                                                        CleanRune()
                                                                                        tenta +=1          
                                                                                        return False, tenta, tenta_plus         
                                                                                else :
                                                                                    time.sleep(0.15)
                                                                                    type_rune, indicatif = selectRune5('pm') # Ga Pa
                                                                                    tenta +=1 
                                                                                    CleanRune()
                                                                                    time.sleep(0.25)
                                                                                    list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                                    if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                                                                                        OtherItem(nombre_item)    
                                                                                return False, tenta, tenta_plus 