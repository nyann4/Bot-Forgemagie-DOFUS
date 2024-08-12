import time
from Macro1 import * 
from MainScreen import screen
from Reconnect import *
import json

def UpStat3(list_value, poid, nombre_item, tenta, tenta_plus, pui, nom_item, nombre_ligne_item, over):
  try :
    A = int(list_value[0])
    B = int(list_value[1])
    C = int(list_value[2])
    D = int(list_value[3])
    E = int(list_value[4])
    F = int(list_value[5])
    G = int(list_value[6])
  except KeyError:
    time.sleep(2)
    pyautogui.click(919,582)
    return type_rune, indicatif, False, tenta, tenta_plus, over
  print('over =', over)
  print(A, B, C, D, E, F, G)  

  path = "C:\\Users\\yannf\\OneDrive\\SWSetup\\Bureau\\PROJET0\\CODE\\all_codes\\DictionnaireItem\\item.json"
  with open(path, encoding='utf-8') as outfile:
    data =json.load(outfile)
  if not (D == 1) and (A < 351 and B < 76) : #portée
    type_rune, indicatif = selectRune(1,4, data, nom_item)
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (G > 5 and G < 9) and (A < 351 and B < 76): #ret pm
    if (G < 5) :
      type_rune, indicatif = selectRune(2,7, data, nom_item) 
    if (G > 4 and G < 8) :
      type_rune, indicatif = selectRune(1,7, data, nom_item)
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (C > 33) and (A < 351 and B < 76) : #sagesse
    if (C == 0) or (C > 7 and C < 11) or (C > 16 and C < 21) :
      type_rune, indicatif = selectRune(3,3, data, nom_item) 
    if (C > 0 and C < 8 ) or (C > 10 and C < 17) or (C > 20 and C < 36)  :
      type_rune, indicatif = selectRune(2,3, data, nom_item) 
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (E > 13 and E < 16) and (A < 351 and B < 76): #dommage feu
    if E < 12 :
      type_rune, indicatif = selectRune(2,5, data, nom_item) 
    if (E > 11 and E < 15) :
      type_rune, indicatif = selectRune(1,5, data, nom_item) 
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (F == 14 or  F == 15) and (A < 351 and B < 76): #tacle
    if F < 12 :
      type_rune, indicatif = selectRune(2,6, data, nom_item) 
    if (F > 11 and F < 15) :
      type_rune, indicatif = selectRune(1,6, data, nom_item) 
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (B > 69 and B < 76) and A < 351 : #intelligence
    if (B > 4 and B < 13 ) or (B > 35 and B < 43) or (B > 45 and B < 53) or (B > 57 and B < 60) :
        type_rune, indicatif = selectRune(2,2, data, nom_item)
    elif (B == 0) or (B > 0 and B < 6)  or (B > 12 and B < 36) or (B > 42 and B < 46) or (B > 52 and B < 58) or (B > 59 and B < 70) :
        type_rune, indicatif = selectRune(3,2, data, nom_item)
    elif B == 76 :
      type_rune, indicatif = selectRune5('ini')
    elif (B > 76) :
      if E < 15 :
        type_rune, indicatif = selectRune(1,5, data, nom_item) 
      elif F < 15 :
        type_rune, indicatif = selectRune(1,6, data, nom_item) 
      else :
        type_rune, indicatif = selectRune5('refeu')
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (A > 339 and A < 351) and over == 0: #vitalité
    indicatif = 0
    if (A < 101) or (A > 139 and A < 169) or (A > 194 and A < 210) or (A > 239 and A < 266) or (A > 289 and A < 340):  
        type_rune, indicatif = selectRune(3,1, data, nom_item)
    elif (A > 100 and A < 140) or (A > 168 and A < 195) or (A > 209 and A < 240) or (A > 265 and A < 290) :
        type_rune, indicatif = selectRune(2,1, data, nom_item)
    elif (A > 350 and A < 500) :
        if A < 356 :
            type_rune, indicatif = selectRune5('ini')
        elif (A > 355 and A < 366) :
            type_rune, indicatif = selectRune5('refeu')
        elif (A > 365 and A < 371) :
            if F < 15:
              type_rune, indicatif = selectRune(1,6, data, nom_item)
            else :
              type_rune = 2
              type_rune, indicatif = selectRune5('refeu')
        elif (A > 370 and A < 381) :
            if E < 15 :
              type_rune, indicatif = selectRune(1,5, data, nom_item)
            else : 
              type_rune, indicatif = selectRune5('refeu')
        elif (A > 380 and A < 386):
            if  G < 8 :
              type_rune, indicatif = selectRune(1,7, data, nom_item)
            else :
              type_rune, indicatif = selectRune5('refeu')
        elif (A > 385) :
          type_rune, indicatif = selectRune5('refeu')
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if not (E > 14 and E < 16) and (A < 351 and B < 76): #dommage feu
    type_rune = 5
    type_rune, indicatif = selectRune(1,5, data, nom_item) 
    return type_rune, indicatif, False, tenta, tenta_plus, over 
  if (A > 339 ) and (B > 69 ) and (C > 33 and C < 41) and (D == 1) and (E > 13 and E < 16) and (F > 13 and F < 16) and (G > 5 and G < 9) :
    if poid > 0 :
      over = 1
    type_rune =  5
    if not (E > 14 ) and type_rune <= poid: #do feu
      type_rune, indicatif = selectRune(1,5, data, nom_item)   
      return type_rune, indicatif, False, tenta, tenta_plus, over 
    type_rune = 7
    if not G > 6 and type_rune <= poid:
      type_rune, indicatif = selectRune(1,7, data, nom_item)
      return type_rune, indicatif, False, tenta, tenta_plus, over 
    type_rune = 9
    if not C > 35 and type_rune <= poid :
      type_rune, indicatif = selectRune(2,3, data, nom_item)
      return type_rune, indicatif, False, tenta, tenta_plus, over 
    type_rune = 4
    if not F > 14 and type_rune <= poid :
      type_rune, indicatif = selectRune(1,6, data, nom_item)
      return type_rune, indicatif, False, tenta, tenta_plus, over 
    type_rune = 10
    print('here')
    if not A > 355  and type_rune <= poid:
      if A < 356:
        type_rune, indicatif = selectRune(3,1, data, nom_item)
      return type_rune, indicatif, False, tenta, tenta_plus, over 
    type_rune = 3
    if not A > 355  and type_rune <= poid:
      if A < 356:
        type_rune, indicatif = selectRune(2,1, data, nom_item)
      return type_rune, indicatif, False, tenta, tenta_plus, over 
  if (A > 339 ) and (B > 69 ) and (C > 33 and C < 41) and (D == 1) and (E > 13 and E < 16) and (F > 13 and F < 16) and (G > 5 and G < 9) :
    indicatif =0
    over = 0
    list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
    if list_1[0].find('PA') != -1 or  list_1[0].find('PM') != -1 or list_1[1].find('PA') != -1 or  list_1[1].find('PM') != -1 :
      OtherItem(nombre_item)
      time.sleep(1)
    else :
      type_rune = 90
      if sum(pui) >= 480 :
          tenta_plus += 1
      tenta += 1
      exo  =0
      suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data)
      type_rune, indicatif = selectRune5('pm')
      list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
      if list_1[0].find('PA') != -1 or  list_1[0].find('PM') != -1 or list_1[1].find('PA') != -1 or  list_1[1].find('PM') != -1 :
        OtherItem(nombre_item)
        time.sleep(1)                                   
    return type_rune, indicatif, False, tenta, tenta_plus, over 