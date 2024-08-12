from random import *
from Macro1 import * 
from screen import screenValues
from MainScreen import *
import random

def UpStats(list_value, nombre_item, tenta, tenta_plus, tenta_4to5crit, fortofive, nombre_ligne_item):
  try :
    A = int(list_value[0])
    B = int(list_value[1])
    C = int(list_value[2])
    D = int(list_value[3])
    E = int(list_value[4])
  except KeyError:
    time.sleep(2)
    pyautogui.click(919,582)
    return  False, tenta, tenta_plus
  print(A, B, C, D, E)
  if not (E > 8) and (A < 251 and B < 101):
      selectRune4(1083,518)
      return False, tenta,tenta_plus, tenta_4to5crit
  else :
      if not (B > 69 ) and (A < 251 and E < 11):
          if B < 8 or (B > 10 and B < 18) or (B > 20 and B < 28) or (B > 30 and B < 38) or (B > 40 and B < 48) or (B > 50 and B < 58): #PaCha
            selectRune4(1136, 394)  
          if (B > 7 and B < 11) or (B > 17 and B < 21) or (B > 27 and B < 31) or (B > 37 and B < 41) or (B > 47 and B < 51) or (B > 57 and B < 70 ):#RaCha
            selectRune4(1187, 394)
          return False, tenta,tenta_plus, tenta_4to5crit
      else :
          if not (C > 2 ) and (A < 251 and B < 101 and E < 11) :
              selectRune4(1085, 435) # crit
              return False, tenta,tenta_plus, tenta_4to5crit
          else : 
              if not (D > 15 ) and (A < 251 and B < 101 and E < 11):
                  if D < 15 :#padoeau
                    selectRune4(1135, 478)
                  if D == 15 :  #do eau
                    selectRune4(1084,479)        
                  return False, tenta,tenta_plus, tenta_4to5crit
              else :
                if not (A > 179 ) and (B < 101 and E < 11) :
                    if (A == 0 ) or (A > 0 and A < 101) or (A > 144 and A < 165) :
                        selectRune4(1187, 355) # ravi
                    if (A > 100 and A < 145) or (A > 164 and A < 180) :
                        selectRune4(1135, 358) # pa vi
                    return False, tenta,tenta_plus, tenta_4to5crit
                else : 
                  if not (B > 91 and B < 101) and (A < 251 and E < 11) :
                    if B < 101 :
                      if (B == 91 ):
                        list_1 = screen(750, 541, 200, 37, 2)
                        if list_1[0] != '\x0c' :
                          time.sleep(0.15)
                          selectRune5(1075, 1028) #  re feu
                          CleanRune()
                        else :
                          selectRune4(1185, 395) # ra vi
                      if B != 91 :
                        selectRune4(1185, 395)                        
                    if B == 101 :
                        time.sleep(0.15)
                        selectRune5(1034, 1030)
                        CleanRune()
                    return False, tenta,tenta_plus, tenta_4to5crit
                  else : 
                    if not  (E > 9 and E < 11) and (A < 251) and (B < 101):
                      if E < 11:
                        selectRune4(1083,518) #re per eau
                      if E > 10:
                        if D < 20:
                          selectRune4(1083, 478) #doeau
                        else : 
                          selectRune5(1075, 1028)
                          CleanRune()
                      return False, tenta,tenta_plus, tenta_4to5crit
                    else : 
                      if not C > 3 and (A < 251 and B < 101 and E < 11) :
                        if C < 6 :
                          selectRune4(1085, 435)
                        return False, tenta,tenta_plus, tenta_4to5crit
                      else : 
                        if not (A > 239 and A < 251) :
                            if (A > 178 and A < 190) or (A > 205 and A < 240) :
                              selectRune4(1135, 358)
                            elif (A > 189 and A < 206) :
                              selectRune4(1187, 355)
                            elif A > 250 :
                              if (A > 250 and A < 256):
                                time.sleep(0.15)
                                selectRune5(1035, 1030)#ini
                                CleanRune()
                              if (A > 255 and A < 271):
                                time.sleep(0.15)
                                selectRune5(1080, 1030)     
                                CleanRune() #re fixe
                              if (A > 270) and D != 20 :
                                selectRune4(1084,479)    
                              if A > 275 : 
                                selectRune4(1083,518) 
                            return False, tenta,tenta_plus, tenta_4to5crit
                        else :
                          if not D > 17 and (A < 251 and B < 101) :
                            if (D == 16 or D == 17) : 
                              selectRune4(1137, 472)
                            return False, tenta,tenta_plus, tenta_4to5crit
                          else : 
                            if fortofive == True:
                              if not C > 4 and (A < 251 and B < 101 and E < 11) :
                                selectRune4(1083, 436)
                                tenta_4to5crit +=1
                                return False, tenta, tenta_plus, tenta_4to5crit
                              else :
                                if (A > 239 ) and (B > 91 and B < 101) and (C > 4 and C < 6) and (D > 17 and D < 21) and (E > 9) :
                                      with open('suivis_anneau_volkorne.txt', 'a') as filehandle:
                                        list_value.insert(0, "n°{}    ".format(tenta))
                                        list_value.insert(0,'\n')
                                        list_value.append(tenta_4to5crit)
                                        filehandle.write(" ".join(str(item) for item in (list_value)))
                                      tenta_4to5crit = 0
                          if (A > 239 ) and (B > 91 and B < 101) and (C > 3 and C < 6) and (D > 17 and D < 21) and (E > 9) :
                                list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                if list_1[0] != '\x0c' or (E > 10 and E <12) :
                                  if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                                    OtherItem(nombre_item) 
                                  else:
                                    selectRune5(1166, 1030) # PM
                                    CleanRune()
                                    tenta +=1          
                                  return False, tenta,tenta_plus, tenta_4to5crit           
                                else :
                                  time.sleep(0.15)
                                  selectRune5(1212, 1030)
                                  tenta +=1 
                                  CleanRune()
                                  time.sleep(0.25)
                                  list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
                                  if list_1[0].find('PM') != -1  or list_1[1].find('PM') != -1 or list_1[0].find('PA') != -1  or list_1[1].find('PA') != -1:
                                    OtherItem(nombre_item)    
                                  return False, tenta,tenta_plus, tenta_4to5crit