import time
import re
from Macro1 import * 
from screen import screenValues
from MainScreen import screen

def UpStats(list_value, pui, count, pui_available, supposed_value, result,number_line):
  # attribuation des variables en fonction de leur ligne
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
   
  if count == 0 : #ecrit le pui de l'item avant le passage de la première rune pour définir une base 
    with open('listfile.txt', 'w') as filehandle:
      filehandle.writelines("%s\n" % place for place in pui)
    pui_available = 0
  else :
    old_stat = []
    with open('listfile.txt', 'r') as filehandle: #lit le pui présent a la rune précédente et l'inscrit dans une liste pour faire des calculs entres le nouveau et l'ancien pui
      filecontents = filehandle.readlines()
      for line in filecontents:
          current_place = float(line[:-1])
          # print("currentplace", current_place)
          old_stat.append(current_place)
          # print("oldstat",old_stat)

    print(old_stat)
    new_total = round((sum(old_stat)),4 ) #fait le total de l'ancien pui
    print('new_total :',new_total)  
    print('supposed_value :', supposed_value)
    abs_sum = round((float(sum(pui))), 4) - (float(sum(old_stat)) + float(supposed_value)) #fait la différence entre le pui actuel et l'ancien pui grace a la valeur de la rune passée
    # correspondant a l'augmentation de pui attendu : ex pui = 100 , rune = 5 , passage rune, pui = 98 , attendu : 105 différence 7 
    print('pui :',pui_available)
    print('difference pui ancien jet/jet attendu :' , abs_sum)
    if number_line == 1000 or number_line == 500:  #evite les erreurs de calculs de pui disponible lors du passage de runes n'étant a l'origine pas présentent sur l'item ex : PM, Re feu
      pui_available += 0 # dans les deux cas présents (voir programme "Macro1") le pui ne dois pas changer
    elif number_line == 750 : # autre cas dans lequel la rune fais échec
      effect = 2
    else : 
      if pui[number_line] - old_stat[number_line] <= 0 : #différence entre une nouvelle et une ancien stats, au cas ou la rune est passé mais a fais baisser le pui 
        # ex : pui = 100 , rune = 6 , passage rune // pui = 98 mais la rune est passé -> différence de pui sur le reste de litem est de : 100 +6 -98 +6 = 14 , la rune dois être compté 2 fois
        effect = 2
      else : 
        effect = 1
    # print('effect', effect)
    if abs_sum == 0 and result == 2: # si il n'y  a pas de différence de pui et le mot reliquat est présent, la rune est passée en succés neutre
      pui_available = pui_available - supposed_value #on retire donc la valeur de la rune au pui disponible
    # if abs_sum == 0 and result == 1:
    #   pui_available = pui_available
    elif abs_sum < 0 and result == 2 : 
      pui_available = pui_available + (int(abs(abs_sum)) - int(supposed_value*effect))
    # elif abs_sum < 0 and result == 1 : 
    #   pui_available = pui_available
    # print('pui :',pui_available)
    with open('listfile.txt', 'w') as filehandle:
      filehandle.writelines("%s\n" % place for place in pui)



  if not E > 0  and (A < 251 and B < 61 and C < 61 and H <401 ):  ###1###1### Portée
    if A ==0 and B == 0 and C == 0 and D == 0 and E == 0 and F == 0 :
      time.sleep(10000)
      print('Problème Theme')
    else :
      type_rune = 51
      supposed_value, result, number_line = selectRune3(1083,516, type_rune)
    return supposed_value, result, number_line, False
  else:
    if not D > 29 and (A < 251 and B < 61 and C < 61 and H <401 ): ###1###2### Sagesse
      if D < 20 :
        type_rune = 30 #RaSa
        supposed_value, result, number_line = selectRune3(1183,476, type_rune)
      if D > 19 : #PaSa
        type_rune = 9 
        supposed_value, result, number_line = selectRune3(1131,476, type_rune)
      return supposed_value, result, number_line, False
    else :
      if not I > 4 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###3### % Résistance neutre
        type_rune = 6
        supposed_value, result, number_line = selectRune3(1083,676, type_rune)
        return supposed_value, result, number_line, False
      else : 
        if not H > 299 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###4### Initiative
          if H < 201  or H > 270:
            type_rune = 10 #RaIni
            supposed_value, result, number_line = selectRune3(1183,636, type_rune)
          if H > 200 and H < 271 :
            type_rune = 3  #PaIni
            supposed_value, result, number_line = selectRune3(1131,636, type_rune)
          return supposed_value, result, number_line, False
        else : 
          if not B > 46 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###5### Chance 
            if B == 10 or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) :
              type_rune = 10  # RaCha
              supposed_value, result, number_line = selectRune3(1183,396, type_rune)
            if B < 10 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40) :
              type_rune = 3 #PaCha
              supposed_value, result, number_line = selectRune3(1131,396, type_rune)
            return supposed_value, result, number_line, False
          else : 
            if not F > 9 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###6### Dommages Eau
              if F < 9 :
                type_rune = 15
                supposed_value, result, number_line = selectRune3(1131,556, type_rune)   
              if F > 8 :
                type_rune = 5  
                supposed_value, result, number_line = selectRune3(1083,556, type_rune)  
              return supposed_value, result, number_line, False
            else : 
              if not J > 4 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###7### % Résistance Terre
                type_rune = 6
                supposed_value, result, number_line = selectRune3(1083,716, type_rune)
                return supposed_value, result, number_line, False
              else : 
                if not A > 199 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###8### Vitalité
                  if A < 40 or (A > 50 and A < 90) or (A > 100 and A < 140) or (A > 150 and A < 190) :
                    type_rune = 3  #PaVi
                    supposed_value, result, number_line = selectRune3(1131,356, type_rune)
                  if (A > 39 and A < 51) or (A > 89 and A < 101) or (A > 139 and A < 151) or (A > 189 and A < 200):
                    type_rune = 10 #RaVi
                    supposed_value, result, number_line = selectRune3(1181,356, type_rune)
                  return supposed_value, result, number_line, False
                else : 
                  if not G > 9 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###9### Dommages Air
                    if G < 9 :
                      type_rune = 15 #PaDoAir
                      supposed_value, result, number_line = selectRune3(1131,596, type_rune)   
                    if G > 8 :
                      type_rune = 5  #DoAir
                      supposed_value, result, number_line = selectRune3(1083,596, type_rune)  
                    return supposed_value, result, number_line, False
                  else : 
                    if not L > 1 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###10### Tacle
                      type_rune = 12
                      supposed_value, result, number_line = selectRune3(1131,796, type_rune)
                      return supposed_value, result, number_line, False
                    else : 
                      if not K > 4 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###11### % Résistance Feu
                        type_rune = 6
                        supposed_value, result, number_line = selectRune3(1083,756, type_rune)
                        return supposed_value, result, number_line, False
                      else : 
                        if not C > 46 and (A < 251 and B < 61 and C < 61 and H <401):  ###1###12### Agilité
                          if C == 10 or (C > 17 and C < 21) or (C > 27 and C < 31) or (C > 37 and C < 41) :
                            type_rune = 10  # RaAge
                            supposed_value, result, number_line = selectRune3(1183,436, type_rune)
                          if C < 10 or (C > 10 and C < 18) or (C > 20 and C < 28) or (C > 30 and C < 38) or (C > 40) :
                            type_rune = 3 #PaAge
                            supposed_value, result, number_line = selectRune3(1131,436, type_rune)
                          return supposed_value, result, number_line, False
                        else : 
                          #FIN ETAPE 1###
                          if not I > 5 and (A < 251 and B < 61 and C < 61 and H <401):  ###2###1### % Résistance Neutre
                            type_rune = 6
                            supposed_value, result, number_line = selectRune3(1083,676, type_rune)
                            return supposed_value, result, number_line, False
                          else: 
                            if not  (H > 379 and H < 401) and (A < 251 and B < 61 and C < 61 ):  ###2###2### Inititive
                              if H < 371 :
                                type_rune = 3 
                                supposed_value, result, number_line = selectRune3(1131,636, type_rune)
                              if H >370 and H <390 :
                                type_rune = 1
                                supposed_value, result, number_line = selectRune3(1131,636, type_rune)
                              if H > 400 :
                                if B < 61 :
                                  type_rune = 1 
                                  supposed_value, result, number_line = selectRune3(1083,396, type_rune)
                                elif C < 61 :
                                  type_rune = 1
                                  supposed_value, result, number_line = selectRune3(1083,436, type_rune)
                                elif A < 246 :
                                  type_rune = 1 
                                  supposed_value, result, number_line = selectRune3(1083,356, type_rune)
                                elif C > 59 and B > 59 and A > 245 :
                                  type_rune = 2
                                  supposed_value, result, number_line = selectRune(1085,1034, type_rune)
                                  CleanRune()                                  
                              return supposed_value, result, number_line, False
                            else : 
                              if not D > 31 and (A < 251 and B < 61 and C < 61 and H <401):  ###2###3### Sagesse
                                type_rune = 9 
                                supposed_value, result, number_line = selectRune3(1131,476, type_rune)
                                return supposed_value, result, number_line, False
                              else :
                                if not (G > 10 and G < 13) and (A < 251 and B < 61 and C < 61 and H <401):  ###2###4### Dommages Air
                                  if G < 13 :
                                    type_rune = 5
                                    supposed_value, result, number_line = selectRune3(1083,596, type_rune)
                                  if G > 12 :
                                    type_rune = 2
                                    supposed_value, result, number_line = selectRune(1085,1034, type_rune)
                                    CleanRune()
                                  return supposed_value, result, number_line, False
                                else : 
                                  if not K > 6 and (A < 251 and B < 61 and C < 61 and H <401):  ###2###5### % Résistance Feu
                                    type_rune = 6
                                    supposed_value, result, number_line = selectRune3(1083,756, type_rune)
                                    return supposed_value, result, number_line, False
                                  else : 
                                    if not L > 2 and (A < 251 and B < 61 and C < 61 and H <401):  ###2###6### Tacle
                                      type_rune = 4 
                                      supposed_value, result, number_line = selectRune3(1083,796, type_rune)
                                      return supposed_value, result, number_line, False
                                    else: 
                                        if not (C > 55 and C < 61) and (A < 251 and B < 61 and H <401):
                                          if (C > 46 and C < 52) : ###2###7### agilité
                                            type_rune = 10 
                                            supposed_value, result, number_line = selectRune3(1181,436, type_rune)
                                          if (C > 51  and C < 61):
                                            type_rune = 3 
                                            supposed_value, result, number_line = selectRune3(1131,436, type_rune)
                                          if C > 60 :
                                            if H < 391 :
                                              type_rune = 1
                                              supposed_value, result, number_line = selectRune3(1083,636, type_rune)
                                            elif B < 60 : 
                                              type_rune = 1 
                                              supposed_value, result, number_line = selectRune3(1083,396, type_rune)
                                            elif A < 246 :
                                              type_rune = 1
                                              supposed_value, result, number_line = selectRune3(1081,356, type_rune)
                                            elif L < 5 :
                                              type_rune = 4
                                              supposed_value, result, number_line = selectRune3(1083,796, type_rune)
                                          return supposed_value, result, number_line, False
                                        else :
                                          if not (B > 55 and B < 61)  and (A < 251 and C < 61 and H <401): 
                                            if (B > 46 and B < 52) : ###2###8### Chance
                                              type_rune = 10 
                                              supposed_value, result, number_line = selectRune3(1181,396, type_rune)
                                            if (B > 51 and B < 61):
                                              type_rune = 3 
                                              supposed_value, result, number_line = selectRune3(1131,396, type_rune)
                                            if B > 60 :
                                              if H < 391 :
                                                type_rune = 1
                                                supposed_value, result, number_line = selectRune3(1083,636, type_rune)
                                              elif C < 60 : 
                                                type_rune = 1 
                                                supposed_value, result, number_line = selectRune3(1083,436, type_rune)
                                              elif A < 246 :
                                                type_rune = 1
                                                supposed_value, result, number_line = selectRune3(1081,356, type_rune)
                                              else :
                                                type_rune = 4
                                                supposed_value, result, number_line = selectRune(1085,1034, type_rune)
                                                CleanRune()
                                            return supposed_value, result, number_line, False
                                          else: 
                                                  if not (A > 239 and A < 251) and (B < 61 and C < 61 and H <401):  ###2###9### Vitalité
                                                    if (A > 199 and  A < 206) :
                                                      type_rune = 10 #RaVi
                                                      supposed_value, result, number_line = selectRune3(1181,356, type_rune)
                                                    if (A > 205 and A < 240) :
                                                      type_rune = 3 # PaVi
                                                      supposed_value, result, number_line = selectRune3(1131,356, type_rune)
                                                    if (A > 250 and A < 256) :
                                                      if B < 60 :
                                                        type_rune = 1 #Cha
                                                        supposed_value, result, number_line = selectRune3(1083,396, type_rune)
                                                      elif C < 60 :
                                                        type_rune = 1 #Age
                                                        supposed_value, result, number_line = selectRune3(1083,436, type_rune)
                                                      elif H < 391 :
                                                        type_rune = 1 #Initiative
                                                        supposed_value, result, number_line = selectRune3(1083,636, type_rune)
                                                    if A > 255 :
                                                      type_rune = 2
                                                      supposed_value, result, number_line = selectRune(1085,1034, type_rune)
                                                      CleanRune()
                                                    return supposed_value, result, number_line, False
                                                  else : 
                                                    if not (F > 10 and F < 13) and (A < 251 and B < 61 and C < 61 and H <401):  ###2###10### Dommages Eau
                                                      if F < 13 :
                                                        type_rune = 5
                                                        supposed_value, result, number_line = selectRune3(1083,556, type_rune)
                                                      if F > 12 :
                                                        type_rune = 2
                                                        supposed_value, result, number_line = selectRune(1085,1034, type_rune)
                                                        CleanRune()
                                                      return supposed_value, result, number_line, False
                                                  
                                                    else :                                                    
                                                        if not (L > 3 and L < 6) and (A < 251 and B < 61 and C < 61 and H <401):  ###2###11### Tacle
                                                          type_rune = 4 
                                                          supposed_value, result, number_line = selectRune3(1083,796, type_rune) 
                                                          return supposed_value, result, number_line, False
                                                        else : 
                                                          if not J > 6 and (A < 251 and B < 61 and C < 61 and H <401):  ###2###12### % Résistance Terre
                                                            type_rune = 6
                                                            supposed_value, result, number_line = selectRune3(1083,716, type_rune)
                                                            return supposed_value, result, number_line, False
                                                          else : 
                                                            if not I > 6 and (A < 251 and B < 61 and C < 61 and H <401):  ###2###13### % Résistance Neutre
                                                              if I < 8 :
                                                                type_rune = 6
                                                                supposed_value, result, number_line = selectRune3(1083,676, type_rune)
                                                              if I > 7 :
                                                                type_rune = 2
                                                                supposed_value, result, number_line = selectRune(1085,1034, type_rune)
                                                                CleanRune()
                                                              return supposed_value, result, number_line, False                                                                                            
                                                            else : 
                                                              if (A > 239 and A < 251) and (B > 55 and B < 61) and (C > 55 and C < 61) and (D > 31 and D < 41) and (E ==1) and (F > 10 and F < 13) and (G > 10 and G < 13) and ( H> 379 and H < 401)and (I > 6 and I < 8) and (J > 6 and J < 8) and (K > 6 and K < 8) and (L > 3 and L < 6):
                                                                list_1 = screen(760, 822, 200, 37, 1)
                                                                # print(list_1[0])
                                                                if list_1[0].find('PM') != -1 or list_1[0].find('PA') != -1 :
                                                                  print(list_1[0])
                                                                  OtherB(1490 ,210)
                                                                  list_1 = screen(760, 621, 200, 37, 1)
                                                                  string = list_1[0]
                                                                  if string.find('Prospection') != -1 :
                                                                    pyautogui.moveTo(642,639, duration=0.5)
                                                                    pyautogui.click(clicks=1) 
                                                                  return supposed_value, result, number_line, False                                  
                                                                else :
                                                                  type_rune = 90
                                                                  supposed_value, result, number_line = selectRune(1212, 1030, type_rune)
                                                                  CleanRune()
                                                                  list_1 = screen(760, 846, 200, 37, 2)
                                                                  if list_1[0].find('PM') != -1 or list_1[0].find('PA') != -1 :
                                                                    OtherB(1490 ,210)
                                                                  list_1 = screen(760, 621, 200, 37, 1)
                                                                  string = list_1[0]
                                                                  if string.find('Prospection') != -1 :
                                                                    pyautogui.moveTo(642,639, duration=0.5)
                                                                    pyautogui.click(clicks=1)
                                                                  return supposed_value, result, number_line, False