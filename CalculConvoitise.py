import re
from Macro1 import * 
from screen import screenValues
from MainScreen import *

def UpStats(list_value):
  
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

    print(A, B, C, D, E, F, G, H, I, J, K)
    if not D > 15 and A < 301 :
        if D < 10 :
            selectRune2(1183, 478)
        else :
            selectRune2(1131, 478)
        return False
    else:
        if not F > 5 and A < 301 :
            if F < 5:
                selectRune2(1131, 561)
            if F == 5 :
                selectRune2(1083, 561)  
            return False
        else:
            if not B > 34 and A < 301 :
                if (B < 8) or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 35):
                    selectRune2(1131, 395)
                if (B > 7 and B < 11) or (B > 17 and B < 21) or (B > 27 and B < 31):
                    selectRune2(1181, 395)
                return False
            else : 
                if not G > 5 and A < 301 :
                    if G < 5:
                        selectRune2(1131, 600)
                    if G == 5 :
                        selectRune2(1083, 600)
                    return False
                else : 
                    if not C > 34 and A < 301 :
                        if (C < 8) or (C > 10 and C < 18) or (C > 20 and C < 28) or (C > 30 and C < 35):
                            selectRune2(1131, 437)
                        if (C > 7 and C < 11) or (C > 17 and C < 21) or (C > 27 and C < 31):
                            selectRune2(1181, 437)
                        return False
                    else : 
                        if not (A > 189 ) :
                            if (A > 39 and A < 51) or (A > 89 and A < 101) or (A > 139 and A < 151) :
                                selectRune2(1187, 355)
                            else :
                                selectRune2(1135, 358)
                            return False
                        else :
                            if not J > 5 and A < 301 :
                                if J < 5:
                                    selectRune2(1131, 721)
                                if J == 5 :
                                    selectRune2(1083, 721)
                                return False
                            else :
                                if not E > 2 and A < 301 :
                                    selectRune2(1083, 520)
                                    return False
                                else : 
                                    if not H > 6 and A < 301 :
                                        selectRune2(1083, 640)
                                        return False
                                    else:
                                        if not K > 5 and A < 301 :
                                            if K < 5:
                                                selectRune2(1131, 764)
                                            if K == 5 :
                                                selectRune2(1083, 764)
                                            return False  #Fin étape 1 ###########
                                        else :
                                            if not D > 23 and A < 301 :
                                                selectRune2(1131, 478)
                                                return False
                                            else:
                                                if not F > 8 and A < 301 :
                                                    if F > 6:
                                                        selectRune2(1081, 561)
                                                    if F == 6 :
                                                        selectRune2(1131, 561)  
                                                    return False
                                                else:
                                                    if not B > 45 and A < 301 :
                                                        if (B > 34 and B < 38) or (B > 40 ) :
                                                            selectRune2(1131, 395)
                                                        if (B > 37 and B < 41) :
                                                            selectRune2(1181, 395)
                                                        return False
                                                    else : 
                                                        if not G > 8 and A < 301 :
                                                            if G > 6:
                                                                selectRune2(1081, 600)
                                                            if G == 6 :
                                                                selectRune2(1131, 600)
                                                            return False
                                                        else : 
                                                            if not C > 45 and A < 301 :
                                                                if (C > 34 and C < 38) or (C > 40 ) :
                                                                    selectRune2(1131, 437)
                                                                if (C > 37 and C < 41) :
                                                                    selectRune2(1181, 437)
                                                                return False
                                                            else : 
                                                                if not (A > 289  and A < 301) :
                                                                    if (A > 189 and A < 206) or (A > 239 and A < 256) :
                                                                        selectRune2(1187, 355)
                                                                    if (A > 205 and A < 240) or (A > 255 and A < 290):
                                                                        selectRune2(1135, 358)
                                                                    if A > 300 :
                                                                        selectRune(1030, 1030)
                                                                        CleanRune()
                                                                    return False
                                                                else :
                                                                    if not J > 7 and A < 301 :
                                                                        selectRune2(1081, 721)
                                                                        return False
                                                                    else : 
                                                                        if not H > 9 and A < 301 :
                                                                            selectRune2(1083, 640)
                                                                            return False
                                                                        else:
                                                                            if not K > 8 and A < 301 :
                                                                                if K > 6 :
                                                                                    selectRune2(1081, 764)
                                                                                if K == 6 :
                                                                                    selectRune2(1131, 764) 
                                                                                return False   
                                                                            else :                                       
                                                                                if (A > 289 ) and (B > 45 and B < 51) and (C > 45 and C < 51) and (D > 23 and D < 31) and (E == 3) and (F > 8) and (G > 8) and (H == 10) and (J > 7) and (K > 8) :
                                                                                        list_1 = screen(760, 782, 200, 37, 2)
                                                                                        print(list_1[0])
                                                                                        print(list_1[1])
                                                                                        if list_1[0] == '1PM\n\x0c' or list_1[1] == '1PM\n\x0c' :
                                                                                            OtherF(1410, 210)                              
                                                                                        else :
                                                                                            selectRune(1212, 1030)
                                                                                            CleanRune()
                                                                                            list_1 = screen(760, 782, 200, 37, 2)
                                                                                            if list_1[0] == '1PM\n\x0c' or list_1[1] == '1PM\n\x0c' :
                                                                                                OtherF(1410, 280)    
                                                                                            return False
                                                                                            print(A, B, C, D, E, F, G, H, I, J, K)