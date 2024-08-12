import time
import re
from Macro1 import * 

def UpStats2(list_value, poid, nombre_item, tenta, tenta_plus, pui, nombre_ligne_item):
    A = int(list_value[0])
    B = int(list_value[1])
    C = int(list_value[2])
    D = int(list_value[3])
    E = int(list_value[4])
    F = int(list_value[5])
    G = int(list_value[6])
    H = int(list_value[7])
    I = int(list_value[8])
    print (A, B, C, D, E, G, H, I)

    if (D == 0 ) and (A < 301 and B < 61) :
        indicatif = 3
        type_rune = 51
        selectRune4(1083,476)
        return type_rune, indicatif, False, tenta, tenta_plus
    else :
        if not (H > 2) and (A < 301 and B < 61): 
            indicatif = 7
            type_rune = 21
            selectRune4(1131, 636)
            return type_rune, indicatif, False, tenta, tenta_plus
        else: 
            if not (C > 24) and (A < 301 and B < 61) :
                indicatif = 2
                type_rune = 9
                selectRune4(1131, 436)
                return type_rune, indicatif, False, tenta, tenta_plus
            else :
                if not (E > 9) and (A < 301 and B < 61) :
                    indicatif = 4
                    type_rune = 15
                    selectRune4(1131, 516)
                    return type_rune, indicatif, False, tenta, tenta_plus
                else: 
                    indicatif = 1
                    if not B > 46 and (A < 301):  ##Agilité
                        if B == 10 or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) :
                            type_rune = 10  # RaAge
                            selectRune4(1183,396)
                        if B < 10 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40) :
                            type_rune = 3 #PaAge
                            selectRune4(1131,396)
                        return type_rune, indicatif, False, tenta, tenta_plus
                    else :
                        if not I > 10 and (A < 301 and B < 61) :
                            indicatif = 8
                            type_rune = 6
                            selectRune4(1131, 676)
                            return type_rune, indicatif, False, tenta, tenta_plus 
                        else :
                            indicatif = 0
                            if not (A > 199):
                                if (A < 101) or (A > 145 and A < 169) or (A > 189 and A < 200):
                                    type_rune = 10
                                    selectRune4(1183, 356)
                                elif (A > 100 and A < 146) or (A > 168 and A < 190) :
                                    type_rune = 3
                                    selectRune4(1131, 356)
                                return type_rune, indicatif, False, tenta, tenta_plus
                                #fin étape 1
                            else : 
                                if not (H > 4 and H < 7) and (A < 301 and B < 61): 
                                    indicatif = 7
                                    type_rune = 7
                                    selectRune4(1083, 636)
                                    return type_rune, indicatif, False, tenta, tenta_plus
                                else:
                                    if not (C > 34 and C < 41) and (A < 301 and B < 61) :
                                        indicatif = 2
                                        type_rune = 9
                                        selectRune4(1131, 436) 
                                        return type_rune, indicatif, False, tenta, tenta_plus
                                    else :
                                        if not (E > 13 and E < 16) and (A < 301 and B < 61):
                                            indicatif = 4
                                            if E == 10 or E == 12 or E == 13 :
                                                type_rune = 5
                                                selectRune4(1083, 516) 
                                            else : 
                                                type_rune = 15
                                                selectRune4(1131, 516)
                                            return type_rune, indicatif, False, tenta, tenta_plus
                                        else : 
                                                if not (G > 9) and (A < 301 and B < 61):
                                                    indicatif = 6
                                                    type_rune = 6
                                                    selectRune4(1083, 596)
                                                    return type_rune, indicatif, False, tenta, tenta_plus
                                                else:
                                                    if not (B > 55 and B < 61) and (A < 301) :
                                                        indicatif = 1
                                                        if B == 40  or (B > 47 and B < 53) :
                                                            type_rune = 10
                                                            selectRune4(1183, 396) #RaAge
                                                        elif (B > 40 and B < 48)  or (B > 52 and B <56):
                                                            type_rune = 3
                                                            selectRune4(1131, 396) #PaAge
                                                        elif (B == 61) :
                                                            if A < 296 :
                                                                indicatif = 0
                                                                type_rune = 1
                                                                selectRune4(1083, 356)
                                                            elif I < 15 :
                                                                indicatif = 8
                                                                type_rune = 2
                                                                selectRune4(1083, 676)
                                                            else : 
                                                                type_rune = 1
                                                                selectRune5(1040,1034) #ini
                                                                CleanRune()
                                                        elif (B == 62) : 
                                                            if I < 15 :
                                                                indicatif = 8
                                                                type_rune = 2
                                                                selectRune4(1083, 676)
                                                            elif A < 286 :
                                                                indicatif = 0
                                                                type_rune = 3
                                                                selectRune4(1083, 356)
                                                            else:
                                                                type_rune = 2
                                                                selectRune5(1083, 1034)
                                                                CleanRune()   
                                                        elif (B == 63) :
                                                            if A < 286 :
                                                                indicatif = 0
                                                                type_rune = 3
                                                                selectRune4(1083, 356)
                                                            if D < 15:
                                                                indicatif = 4
                                                                type_rune = 5
                                                                selectRune4(1083, 516)
                                                            else : 
                                                                type_rune = 2
                                                                selectRune5(1083, 1034)
                                                                CleanRune()
                                                        elif (B > 63) :
                                                            if D < 15 :
                                                                indicatif = 4
                                                                type_rune = 5
                                                                selectRune4(1083, 516)
                                                            elif F < 10 :
                                                                indicatif = 6
                                                                type_rune = 6
                                                                selectRune4(1083, 596)
                                                            else : 
                                                                type_rune = 2
                                                                selectRune5(1083, 1034)
                                                                CleanRune()
                                                        return type_rune, indicatif, False, tenta, tenta_plus
                                                    else : 
                                                        if not (I > 14 and I < 16) and (A < 301 and B < 61) :
                                                            indicatif = 8
                                                            if I ==11 :
                                                                type_rune = 6
                                                                selectRune4(1131, 676)
                                                            else :
                                                                type_rune = 2
                                                                selectRune4(1083, 676)
                                                            if (I > 15):
                                                                type_rune = 2
                                                                selectRune5(1083,1030)
                                                                CleanRune()
                                                            return type_rune, indicatif, False, tenta, tenta_plus
                                                        else:
                                                            if not (A > 289 and A < 301) and (B < 61):
                                                                indicatif = 0
                                                                if (A > 199 and A < 206) or (A > 239 and A < 256) :# entre 0 et 100 ou entre 145 et 168   
                                                                    type_rune = 10  
                                                                    selectRune4(1183, 356) #RaVi
                                                                elif (A > 205 and A < 240) or (A > 255 and A < 291) :
                                                                    type_rune = 3
                                                                    selectRune4(1131, 356) #PaVi
                                                                elif A > 300 :
                                                                    if A < 306 :
                                                                        if B < 60 :
                                                                            indicatif = 1
                                                                            type_rune = 1
                                                                            selectRune4(1083, 396)
                                                                        else : 
                                                                            type_rune = 1
                                                                            selectRune5(1040, 1030)
                                                                            CleanRune()
                                                                    if A > 305 :
                                                                        if I < 15:
                                                                            indicatif = 8
                                                                            type_rune = 2
                                                                            selectRune4(1083, 676)
                                                                        else:
                                                                            type_rune = 2
                                                                            selectRune5(1083, 1034)
                                                                            CleanRune()
                                                                return type_rune, indicatif, False, tenta, tenta_plus
                                                            else:
                                                                if (A > 289 and A < 356) and (B > 55 and B < 61) and (C > 34 and C < 41) and (D == 1) and (E > 13 and E < 16) and (G == 10) and (H > 4 and H < 7)  and (I > 13 and I < 16): 
                                                                    list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                    if list_1[0].find('PA') != -1 or  list_1[0].find('PM') != -1 or list_1[1].find('PA') != -1 or  list_1[1].find('PM') != -1 :
                                                                        type_rune = 90
                                                                        OtherItem(nombre_item)
                                                                        return type_rune, indicatif, False, tenta , tenta_plus
                                                                    else : 
                                                                        type_rune = 5
                                                                        indicatif = 4
                                                                        if not E > 14 and type_rune <= poid:
                                                                            selectRune4(1083, 516)
                                                                            return type_rune, indicatif, False, tenta, tenta_plus
                                                                        else : 
                                                                            type_rune = 3
                                                                            indicatif = 1
                                                                            if not B > 56 and type_rune <= poid:
                                                                                selectRune4(1131, 396)
                                                                                return type_rune, indicatif, False, tenta, tenta_plus
                                                                            else : 
                                                                                type_rune = 7
                                                                                indicatif = 7
                                                                                if not H > 5 and type_rune <= poid:
                                                                                    selectRune4(1083, 636)
                                                                                    return type_rune, indicatif, False, tenta, tenta_plus
                                                                                else : 
                                                                                    type_rune = 9
                                                                                    indicatif = 2
                                                                                    if not C > 37 and type_rune <= poid:
                                                                                        selectRune4(1131, 436)
                                                                                        return type_rune, indicatif, False, tenta, tenta_plus
                                                                                    else : 
                                                                                        list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                                        type_rune = 6
                                                                                        if list_1[0].find('1% Résistance') == -1 and type_rune <= poid:
                                                                                            selectRune5(990, 1034) #RePerAir
                                                                                            CleanRune()
                                                                                            return type_rune, indicatif, False, tenta, tenta_plus
                                                                                        else : 
                                                                                            if (A > 289 and A < 356) and (B > 55 and B < 61) and (C > 34 and C < 41) and (D == 1) and (E > 13 and E < 16) and (G > 9) and (H > 4 and H < 7)  and (I > 13 and I < 16):
                                                                                                list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                                                                                if list_1[0] == '\x0c':
                                                                                                    type_rune = 100
                                                                                                    if sum(pui) >= 480 :
                                                                                                        tenta_plus+=1
                                                                                                    tenta +=1
                                                                                                    selectRune5(1212, 1030)
                                                                                                    CleanRune()
                                                                                                    return type_rune, indicatif, False, tenta, tenta_plus
                                                                                                else :
                                                                                                    if list_1[0].find('1% Résistance') != -1:
                                                                                                        exo = 6
                                                                                                    else : 
                                                                                                        exo = 0
                                                                                                    type_rune = 90
                                                                                                    if sum(pui)+exo >= 480 :
                                                                                                        tenta_plus+=1
                                                                                                    tenta +=1
                                                                                                    selectRune5(1166, 1030)
                                                                                                    CleanRune()
                                                                                                    return type_rune, indicatif, False, tenta, tenta_plus