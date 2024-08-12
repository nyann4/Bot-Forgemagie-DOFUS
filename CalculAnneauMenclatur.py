from soupsieve import select
from Macro1 import * 
from screen import screenValues
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
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return  False, tenta, tenta_plus
    list_value = screenValues(853, 487, 200, 40, 1 )
    if list_value[0].find('rreur') != -1  or list_value[0].find('Attention') != -1:
        time.sleep(2)
        pyautogui.click(919,582)
        return False, tenta, tenta_plus
    print(A, B, C, D, E, F, G, H, I)

    if not (C > 1 ) and (A < 301) and (B < 71):
        selectRune(1,3) #Crit
        return False, tenta, tenta_plus
    if not (B > 49) and (A < 301):
        if (B > 10 and B < 18 ) or (B > 20 and B < 28 ) or (B > 30 and B < 38 ) or (B > 40 and B < 46) :
            selectRune(2,2) #PaAge
        elif (B == 0) or (B > 0 and B < 11)  or (B > 17 and B < 21) or (B > 27 and B < 31)or (B > 37 and B < 41) or (B > 45 and B < 50) :
            selectRune(3,2)  #RaAge
        return False, tenta, tenta_plus
    if not (E > 4) and (A < 301) and (B < 71):
        selectRune(1,5) #re per terre
        return False, tenta, tenta_plus
    if not ( D > 5) and (A < 301) and (B < 71):
        if D == 5:
            selectRune(1,4) #DoAir
        else :
            selectRune(2,4) #PaDoAir
        return False, tenta, tenta_plus
    if not (I > 13)and (A < 301) and (B < 71):
        selectRune(2, 9) #PaDoPou
        return False, tenta, tenta_plus
    if not (A > 239) and (A < 301) and (B < 71):
        if (A == 0 ) or (A > 0 and A < 90) or (A > 144 and A < 165) or (A > 205 and A < 240) :
            selectRune(2,1) # PaVi
        if (A > 89 and A < 145) or (A > 164 and A < 206) :
            selectRune(3,1) #RaVi
        return False, tenta, tenta_plus
    if not (F > 4) and (A < 301) and (B < 71):
        selectRune(1,6) #Re Per Air
        return False, tenta, tenta_plus
    if not (H > 2) and (A < 301) and (B < 71):
        if H == 1:
            selectRune(2,8) #PaRePM
        else :
            selectRune(1,8) #RePM
        return False, tenta, tenta_plus 
                        # FIN ETAPE 1 
    if not (C > 2) and (A < 301) and (B < 71):
        selectRune(1,3)
        return False, tenta, tenta_plus
    if not (B > 64 and B < 71) and (A < 301):
        if B == 63 or B == 64:
            R = random.randint(1,4)
            if R == 1 or R == 2 :
                selectRune(3, 2) #RaAge
            else :
                selectRune(2, 2) #PaAge
        if (B > 64 and B < 71):
            selectRune(2,2) #PaAge
        elif B < 63:
            selectRune(3, 2)
        elif B > 60 :
            if B == 71 :
                time.sleep(0.15)
                if A < 296:
                    selectRune(1, 1) #Vi
                else :     
                    time.sleep(0.15)
                    selectRune5(1035,1034) #Ini
                    CleanRune()
            if B == 72 :
                time.sleep(0.15)
                if  A < 286:
                    selectRune(2, 1)
                elif D < 10:
                    selectRune(1,4)
                else :
                    selectRune5(1080,1034) #ReFeu
                    CleanRune()
            if B >72:
                time.sleep(0.15)
                if  A < 286:
                    selectRune(2, 1)
                elif D < 10:
                    selectRune(1,4)
                elif I < 20 :
                    selectRune(1, 9)
                else :
                    selectRune5(1080,1034) #ReFeu
                    CleanRune()
        return False, tenta, tenta_plus
    if not (E > 5) and (A < 301) and (B < 71): 
        selectRune(1,5) #Re Per Terre
        return False, tenta, tenta_plus
    if not (A > 289 and A < 301) and B < 71: 
        if A < 301:
            if (A > 239 and A < 260) or (A > 270 and A < 275) or (A > 285):
                selectRune(3, 1) # ravi
            if (A > 259 and A < 271) or (A > 274 and A < 286): 
                selectRune(2, 1) # pavi
        else :
            if A > 300 and A < 306:
                selectRune5(1045, 1030) #ini
                CleanRune()
            elif A > 305 and A < 316:
                if B < 68 :
                    selectRune(2, 2) #PaAge
                else : 
                    type_rune = 2
                    selectRune5(1080, 1030) # refeu
                    CleanRune()
            elif A > 315 and A < 326  :
                if D < 10 : 
                    selectRune(1,4) #DoAir
                else:
                    selectRune5(1080, 1030) #ReFeu
                    CleanRune()
            elif A > 325 :
                if E < 7 :
                    selectRune(1, 5) #RePerTerre
                elif F < 7: 
                    selectRune(1, 6) #RePerAir
                elif D < 10 :
                    selectRune(1, 4) #DoAir
                elif I < 20:
                    selectRune(1, 9) #DoPou
                else:
                    selectRune5(1080, 1030) #ReFeu
                    CleanRune() 
        return False, tenta, tenta_plus 
    if not (E > 6) and ( A < 301) and (B < 71):
        selectRune(1,5) #RePerTerre
        return False, tenta, tenta_plus
    if not (F > 5) and (A < 301) and (B < 71): 
        selectRune(1,6) #RePerAir
        return False, tenta, tenta_plus  
    #FIN ETAPE 2 
    if not (H > 3) and (A < 301) and (B < 71): 
        selectRune(1,8) #RePM
        return False, tenta, tenta_plus
    if not (C > 3) and (A < 301) and (B < 71):
        selectRune(1,3)
        return False, tenta, tenta_plus
    if not (F > 6) and (A < 301) and (B < 71): 
        selectRune(1,6) #RePerAir
        return False, tenta, tenta_plus  
    if not(I > 16) and (A < 301) and (B < 71):
        if I == 14 or I == 15 : 
            selectRune(2,9) #Pa Do Pou
        if I == 16 or I == 17 :
            selectRune(1,9) #DoPou
        return False, tenta, tenta_plus
    if not D > 8 and A < 301 and B < 71:
        if D == 6: 
            selectRune(2, 4) #PaDoAir
        else:
            selectRune(1, 4) #DoAir
        return False, tenta, tenta_plus                     
    if (A > 289 and A < 301) and (B > 64 and B < 71) and (C > 3) and (D > 8) and (E > 6) and (F > 6 ) and (H > 3) and (I > 16): 
        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
        if list_1[0] != '\x0c' :
            if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                OtherItem(nombre_item) 
            else :
                tenta+=1
                time.sleep(0.15)
                selectRune5(1170, 1030)  
                CleanRune()   #Ga PM                    
        else :
            tenta+=1
            time.sleep(0.15)
            selectRune5(1210, 1030) #Ga PA
            CleanRune()
            list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
            if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                OtherItem(nombre_item)    
        return False, tenta, tenta_plus