import time
from weakref import KeyedRef

from soupsieve import select
from Macro1 import * 
from screen import *

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
  print(A, B, C, D, E, F, G, I)

  if not (D > 3) and (A < 251 and B < 61):
    selectRune(1, 4) #Crit
    return False, tenta, tenta_plus
  else :
    if not (E > 5) and (A < 251 and B < 61):
      selectRune(2, 5) #PaDo Neutre 
      return False, tenta, tenta_plus
    else :
      if not (C > 6) and (A < 251 and B < 61 ):
        selectRune(2, 3) #PaSa
        return False, tenta, tenta_plus
      else : 
        if not (A > 149) and (B < 61):
          if (A == 0 ) or (A > 0 and A < 101) or (A > 144 and A < 150) :
            selectRune(3, 1) #Ra Vi
          if (A > 100 and A < 145) :
            selectRune(2, 1) #Pa Vi
          return False, tenta, tenta_plus
        else : 
          if not (F > 5) and (A < 251 and B < 61):
            selectRune(2, 6) #PaDoTerre
            return False, tenta, tenta_plus
          else : 
            if not (B > 39) and (A < 251):
              if (B > 10 and B < 16 ):
                selectRune(2, 2) #PaFo
              elif (B == 0) or (B > 0 and B < 11)  or (B > 15 and B < 41) :
                selectRune(3, 2) #RaFo
              return False, tenta, tenta_plus
            else :
              if not (G > 6) and (A < 251 and B < 61) :
                selectRune(1, 7) #RePerEau
                return False, tenta, tenta_plus
              else: 
                if not (I > 4) and (A < 251 and B < 61) :
                  selectRune(2, 9) #PaDoCrit
                  return False, tenta, tenta_plus
                else :
                #Fin étape 1
                  if not (D > 5) and (A < 251 and B < 61):
                    selectRune(1, 4) # Crit
                    return False, tenta, tenta_plus
                  else : 
                    if not (E > 8) and (A < 251 and B < 61):
                      if (E == 8  or E == 6) :
                        selectRune(2, 5) #PaDoNeutre
                      if E == 7 :
                        selectRune(1, 5) #DoNeutre
                      return False, tenta, tenta_plus
                    else :
                      if not (C > 9) and (A < 251 and B < 61):
                        selectRune(2, 3) #PaSa
                        return False, tenta, tenta_plus
                      else : 
                        if not (A > 189) and (B < 61):
                          if (A > 74 and A < 86) or (A > 124 and A < 140) or (A > 155 and A <171) or (A > 174 and A < 190):
                            selectRune(2, 1)
                          else :
                            selectRune(3, 1)  #RaVi
                          return False, tenta, tenta_plus
                        else : 
                            if not (F > 8) and (A < 251 and B < 61):
                              if (F == 8  or F == 6) :
                                selectRune(2, 6) #PaDoTerre
                              if F == 7 :
                                selectRune(1, 6) #DoTerre
                              return False, tenta, tenta_plus
                            else : 
                              if not (B > 49) and (A  < 251):
                                if B > 39 and B < 46:
                                  selectRune(2, 2) #PaFo
                                if B > 45 :
                                  selectRune(3, 2) #RaFo
                                return False, tenta, tenta_plus
                              else : 
                                if not (G > 8) and (A < 251 and B < 61):
                                  selectRune(1, 7) # RePerEau
                                  return False, tenta, tenta_plus
                                else : 
                                  if not (I > 5) and (A < 251 and B < 61):
                                    if I < 4 :
                                      selectRune(2, 9) #PaDoCrit
                                    else :
                                      selectRune(1, 9) #DoCrit
                                    return False, tenta, tenta_plus
                                  else:
                                    #Fin étape 2 
                                    if not (A > 239 and A < 251)  and (B < 61):
                                      if (A > 189 and A < 211) or (A > 220 and A < 225):
                                        selectRune(3, 1) #RaVi
                                      if (A > 210 and A < 221) or (A > 224 and A < 240):
                                        selectRune(2, 1) #PaVi
                                      if (A > 250 and A < 256) :
                                        if B < 60 :
                                          selectRune(1, 2)
                                        else :
                                          selectRune5(1040, 1030) #Ini
                                          CleanRune()
                                      if (A > 255 and A < 261) :
                                        selectRune5(1080, 1030) #ReFeu
                                        CleanRune()
                                      if (A > 260 and A < 271):
                                        selectRune(1, 3)
                                      if A > 270 :
                                        if F < 12:
                                          selectRune(1, 6) #do terre
                                        elif E < 12 :
                                          selectRune(1, 5) #do neutre
                                        else : 
                                          selectRune(1, 3) # rune sa
                                      return False, tenta, tenta_plus 
                                    else : 
                                      if not (E > 10) and (A < 251 and B < 61) :
                                        if E < 12 :
                                          selectRune(1, 5) #DoNeutre
                                        if E > 12 :
                                          if F < 12 :
                                            selectRune(1, 6) #Do Terre
                                          else : 
                                            selectRune5(1080, 1030) #ReFeu
                                            CleanRune()
                                        return False, tenta, tenta_plus
                                      else :
                                        if not (F > 10) and (A < 251 and B < 61) :
                                          if F < 12 :
                                            selectRune(1, 6) #DoTerre
                                          if F > 12 :
                                            if E <12 :
                                              selectRune(1, 5) #DoNeutre
                                            else : 
                                              selectRune5(1080, 1030) #Refeu
                                              CleanRune()
                                          return False, tenta, tenta_plus 
                                        else : 
                                          if not (D > 6) and (A < 251 and B < 61):
                                            if D < 8 :
                                              selectRune(1, 4) #Crit
                                            if D > 7 :
                                              selectRune(2, 3) #PaSa
                                            return False, tenta, tenta_plus
                                          else :
                                            if not (B > 55 and B < 61) and (A < 251) :
                                              if (B > 49 and B < 56) :
                                                selectRune(3, 2) #RaFo
                                              # if (B > 52 and B < 56) :
                                              #   selectRune(2, 2) #PaFo
                                              if (B == 61) :
                                                if A < 246 :
                                                  selectRune(1, 1) #Rune Vi
                                                else :
                                                  selectRune5(1040, 1030) #Ini
                                                  CleanRune()
                                              if (B == 62) :
                                                selectRune(1, 3) #Sa
                                              if B > 62:
                                                if I == 8 :
                                                  selectRune(1, 9) #do crit
                                                elif F< 11 :
                                                  selectRune(1, 6) #DoTerre
                                                elif E < 11:
                                                  selectRune(1, 5) #DoNeutre
                                                elif F< 12 :
                                                  selectRune(1, 6) #DoTerre
                                                elif E < 12:
                                                  selectRune(1, 5) #DoNeutre
                                              return False, tenta, tenta_plus
                                            else :
                                              if not G > 9 and (A < 251 and B < 61):
                                                if G < 11 :
                                                  selectRune(1, 7)  #RePerEau
                                                if G > 10 :
                                                  selectRune5(1080, 1030) #ReFeu
                                                  CleanRune()
                                                return False, tenta, tenta_plus
                                              else :
                                                if not (C > 9) and (A < 251 and B  < 61):
                                                  if C < 21 :
                                                    if C == 10 : 
                                                      selectRune(1, 3) #Sa
                                                    else :
                                                      selectRune(2, 3) #PaSa
                                                  return False, tenta, tenta_plus
                                                else :
                                                  if not (I > 8 and I < 11) and (A < 251 and B < 61) :
                                                    if I == 6 :
                                                      selectRune(2, 9) #PaDoCrit
                                                    elif I == 7 or I ==8 :
                                                      selectRune(1, 9) #DoCrit
                                                    elif I > 10 :
                                                      if F < 12 :
                                                        selectRune(1, 6) #DoTerre
                                                      elif E < 12 :
                                                        selectRune(1, 5) #DoNeutre
                                                      else : 
                                                        selectRune5(1085, 1030)
                                                        CleanRune()
                                                    return False, tenta, tenta_plus
                                                  else:
                                                      if (A > 239 and A < 251) and (B > 54 and B < 61) and (C > 9 and C < 21) and (D > 6 and D < 8) and (E > 10 and E < 13) and (F > 10 and F < 13) and (G > 9 and G < 12) and (I > 8 and I < 11) : 
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

                                                        #average 89 runes par tenta                                                     