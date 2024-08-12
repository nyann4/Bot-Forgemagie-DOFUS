import re
from Macro1 import * 
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
    except KeyError:
        time.sleep(2)
        pyautogui.click(919,582)
        return  False, tenta, tenta_plus
    print(A, B, C, D, E, F, G, H, I)

    if not (D > 2 ) and (A < 351) and (B < 61):
        selectRune4(1083,476) #Crit
        return False, tenta, tenta_plus
    else:
        if not (B > 49) and (A < 351):
            if (B > 10 and B < 18 ) or (B > 20 and B < 28 ) or (B > 30 and B < 38 ) or (B > 40 and B < 46) :
                selectRune4(1131,396) #PaIne
            elif (B == 0) or (B > 0 and B < 11)  or (B > 17 and B < 21) or (B > 27 and B < 31)or (B > 37 and B < 41) or (B > 45 and B < 50) :
                selectRune4(1183,396)  #RaIne
            return False, tenta, tenta_plus
        else :
            if not (G > 4) and (A < 351) and (B < 61):
                selectRune4(1083,596) #re per terre
                return False, tenta, tenta_plus
            else : 
                if not ( C > 10) and (A < 351) and (B < 61):
                    selectRune4(1131,436) #PaSa
                    return False, tenta, tenta_plus
                else:
                    if not (I > 9)and (A < 351) and (B < 61):
                        if (I == 0 or I == 2 or I == 4 or I == 6 or I == 8):
                            selectRune4(1083,676) #DoCri
                        if (I == 1 or I == 3 or I == 5 or I == 7 or I == 9):
                            selectRune4(1131,676) #PaDoCri
                        return False, tenta, tenta_plus
                    else :
                        if not (A > 239) and (A < 351) and (B < 61):
                            if (A == 0 ) or (A > 0 and A < 90) or (A > 144 and A < 165) or (A > 205 and A < 240) :
                                selectRune4(1131,356) # PaVi
                            if (A > 89 and A < 145) or (A > 164 and A < 206) :
                                selectRune4(1183,356) #RaVi
                            return False, tenta, tenta_plus
                        else:
                            if not (H > 4) and (A < 351) and (B < 61):
                                selectRune4(1083,636) #Re Per Air
                                return False, tenta, tenta_plus
                            else: 
                                if not (E > 5) and (A < 351) and (B < 61):
                                    selectRune4(1131,516) #PaDoFeu
                                    return False, tenta, tenta_plus 
                        # FIN ETAPE 1 
                                else :
                                # return True
                                    if not (D > 3) and (A < 351) and (B < 61):
                                        if D < 4 :
                                            selectRune4(1083,476)
                                        if D > 4 :
                                            time.sleep(0.15)
                                            selectRune5(1035,1034)
                                            CleanRune()
                                        return False, tenta, tenta_plus
                                    else :
                                        if not (B > 54 and B < 61) and (A < 351):
                                            if B == 53:
                                                R = random.randint(1,5)
                                                if R == 1 or R == 2:
                                                    selectRune4(1183, 396)
                                                else :
                                                    selectRune4(1131, 396)
                                            if (B > 53 and B < 61):
                                                selectRune4(1131,396) #PaIne
                                            elif B < 53:
                                                selectRune4(1183, 396)
                                            elif B > 60 :
                                                if B == 61 :
                                                    time.sleep(0.15)
                                                    if A < 346:
                                                        selectRune4(1081, 356)
                                                    else :     
                                                        time.sleep(0.15)
                                                        selectRune5(1035,1034) #Ini
                                                        CleanRune()
                                                if B == 62 :
                                                    time.sleep(0.15)
                                                    if  A < 336:
                                                        selectRune4(1081, 356)
                                                    elif E < 10:
                                                        selectRune4(1083,516)
                                                    else :
                                                        selectRune4(1083, 436)
                                                if B >62:
                                                    time.sleep(0.15)
                                                    if E < 10:
                                                        selectRune4(1083,516)
                                                    elif I < 15 :
                                                        selectRune4(1083, 676)
                                                    else :
                                                        selectRune4(1083, 436)
                                            return False, tenta, tenta_plus
                                        else :
                                            if not (G > 5) and (A < 351) and (B < 61): 
                                                selectRune4(1083,596) #Re Per Terre
                                                return False, tenta, tenta_plus
                                            else :
                                                if not (C > 12)  and (A < 351) and (B < 61):
                                                    selectRune4(1131,436)
                                                    return False, tenta, tenta_plus
                                                else :
                                                    if not(I > 13) and (A < 351) and (B < 61):
                                                        if I == 10 or I == 11 : 
                                                            selectRune4(1131,676) #Pa Do Cri
                                                        if I == 12 or I == 13 :
                                                            selectRune4(1083,676) #Do Cri
                                                        return False, tenta, tenta_plus
                                                    else :
                                                        if not A > 289 :
                                                            if (A > 239 and A < 261) :
                                                                selectRune4(1183,356) #RaVi
                                                            if (A > 260 and A < 290) :
                                                                selectRune4(1131,356) #PaVi
                                                            return False, tenta, tenta_plus
                                                        else : 
                                                            if not (H > 6) and ( A < 351) and (B < 61):
                                                                type_rune = 6
                                                                selectRune4(1083,636) #Re Per Air
                                                                return False, tenta, tenta_plus
                                                            else : 
                                                                if not (E > 7) and (A < 351) and (B < 61):
                                                                    if  E == 7 : 
                                                                        selectRune4(1083,516) #DoFeu
                                                                    elif  E == 5 or E == 6 :
                                                                        selectRune4(1131,516) #Pa Do Feu
                                                                    elif  E > 10 :
                                                                        time.sleep(0.15)
                                                                        selectRune5(990,1034) #ReFeu
                                                                        CleanRune()
                                                                    return False, tenta, tenta_plus
                                                                    #FIN ETAPE 2 
                                                                else :
                                                                    if not (G > 6) and (A < 351) and (B < 61): 
                                                                        if G < 7 :
                                                                            selectRune4(1083,596)
                                                                        if G > 7 : 
                                                                            time.sleep(0.15)
                                                                            selectRune5(1035,1034)
                                                                            CleanRune()
                                                                        return False, tenta, tenta_plus
                                                                    else : 
                                                                        if not (H > 6) and (A < 351) and (B < 61):
                                                                            if H < 7 :
                                                                                selectRune4(1083,636)
                                                                            if H > 7 :
                                                                                time.sleep(0.15)
                                                                                selectRune5(1035,1034)
                                                                                CleanRune()
                                                                            return False, tenta, tenta_plus
                                                                        else:
                                                                            if not (A > 335 and A < 351) : 
                                                                                if A > 289 and A < 316 :
                                                                                    selectRune4(1183,356)
                                                                                if A > 315 and A < 340:
                                                                                    selectRune4(1131,356)
                                                                                if A > 350 :
                                                                                    if (A > 350 and A < 356):
                                                                                        if B < 60 :
                                                                                            time.sleep(0.15)
                                                                                            selectRune4(1083, 396)
                                                                                        else :
                                                                                            time.sleep(0.15)
                                                                                            selectRune5(1035,1034)
                                                                                            CleanRune()
                                                                                    if A > 355 :
                                                                                        time.sleep(0.15)
                                                                                        selectRune5(1035,1034)
                                                                                        CleanRune()
                                                                                return False, tenta, tenta_plus
                                                                            else :                                                        
                                                                                    if (A > 335 and A < 351) and (B > 53 and B < 61) and (C > 12) and (D > 3) and (E > 7) and (G > 6 ) and (H > 6) and (I > 13): 
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