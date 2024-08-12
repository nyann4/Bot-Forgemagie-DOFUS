import time
import re
from Macro1 import * 
from screen import screenValues
from MainScreen import screen
from Reconnect import *
import random

def UpStats2(list_value, poid, nombre_item, nombre_ligne_item, tenta, nom_item, mode, other, pui, min):
  from pathlib import Path
  import json
  from pyautogui import scroll

  vita = int(list_value[0])
  chance = int(list_value[1])
  agilité = int(list_value[2])
  sagesse = int(list_value[3])
  po = int(list_value[4])
  doeau = int(list_value[5])
  doair = int(list_value[6])
  prospe = int(list_value[7])
  ini = int(list_value[8])
  reperneutre = int(list_value[9])
  reperterre = int(list_value[10])
  reperfeu = int(list_value[11])
  tacle = int(list_value[12])
  under1_root_path = Path("..").resolve()
  path_dict_item = under1_root_path / "DictionnaireItem/item.json"
  with open(path_dict_item, encoding='utf-8') as outfile:
      data =json.load(outfile)
  
  tenta_plus, indicatif, done = 0, 0, False
  near_perf = (vita > 239 and chance > 55 and agilité > 55 and sagesse >34 and doeau >10 and doair >10 and reperneutre >6 and reperterre>6 and reperfeu>6 and tacle>3)

  if vita > 250 and not near_perf :
    if chance < 60 :
      type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Cha
    elif agilité < 60 :
      type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Age
    elif ini < 391 :
      type_rune, indicatif, done = selectRune(1,9, data, nom_item) #Ini
    else :
      type_rune, indicatif, other_rune = selectRune5('refeu') 
    return type_rune, indicatif, done, tenta, poid, other

  if not (po > 0)  and ( chance < 61 and agilité < 61 and ini <401 ) and (poid < min): # ligne pour les tenta ++
  # if not (E > 0)  and (chance < 61 and agilité < 61 and ini <401 ) :  ###1###1### Portée
    type_rune, indicatif, done = selectRune(1,5, data, nom_item) #Po
    time.sleep(0.4)
    return type_rune, indicatif, done, tenta, poid, other

  if not sagesse > 29 and (chance < 61 and agilité < 61 and ini <401 ): ###1###2### Sagesse
    if sagesse < 20 :
      type_rune, indicatif, done = selectRune(3,4, data, nom_item) #RaSa
    if sagesse > 19 : #PaSa
      type_rune, indicatif, done = selectRune(2,4, data, nom_item) #PaSa
    return type_rune, indicatif, done, tenta, poid, other

  if not reperneutre > 4 and (chance < 61 and agilité < 61 and ini <401):  ###1###3### % Résistance neutre
    type_rune, indicatif, done = selectRune(1,10, data, nom_item)
    return type_rune, indicatif, done, tenta, poid, other

  if not ini > 299 and (chance < 61 and agilité < 61 and ini <401):  ###1###4### Initiative
    if (ini > 89 and ini < 101) or (ini > 189 and ini < 201) or (ini > 289 and ini < 300)  :
      type_rune, indicatif, done = selectRune(3,9, data, nom_item) #RaIni
    if ini < 71 or (ini > 100 and ini < 171) or (ini > 200 and ini < 271):
      type_rune, indicatif, done = selectRune(2,9, data, nom_item) #PaIni
    if (ini > 70 and ini < 90) or (ini > 170 and ini < 190) or (ini > 270 and ini < 290)  :
      type_rune, indicatif, done = selectRune(1,9, data, nom_item) #Ini
    return type_rune, indicatif, done, tenta, poid, other

  if not chance > 46 and (chance < 61 and agilité < 61 and ini <401):  ###1###5### Chance 
    if chance == 10 or (chance > 17 and chance < 21) or (chance > 27 and chance < 31) or (chance > 37 and chance < 41) :
      type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaCha
    if chance < 10 or (chance > 10 and chance < 18) or (chance > 20 and chance < 28) or (chance > 30 and chance < 38) or (chance > 40) :
      type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaCha
    return type_rune, indicatif, done, tenta, poid, other

  if not doeau > 9 and (chance < 61 and agilité < 61 and ini <401):  ###1###6### Dommages Eau
    if doeau < 9 :
      type_rune, indicatif, done = selectRune(2,6, data, nom_item)  #PaDoEau
    if doeau > 8 :
      type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoEau
    return type_rune, indicatif, done, tenta, poid, other

  if not reperterre > 4 and (chance < 61 and agilité < 61 and ini <401):  ###1###7### % Résistance Terre
    type_rune, indicatif, done = selectRune(1,11, data, nom_item) #RePerTerre
    return type_rune, indicatif, done, tenta, poid, other

  if not vita > 199 and (chance < 61 and agilité < 61 and ini <401):  ###1###8### Vitalité
    if vita < 40 or (vita > 50 and vita < 90) or (vita > 100 and vita < 140) or (vita > 150 and vita < 190) :
      type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
    if (vita > 39 and vita < 51) or (vita > 89 and vita < 101) or (vita > 139 and vita < 151) or (vita > 189 and vita < 200):
      type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
    return type_rune, indicatif, done, tenta, poid, other

  if not doair > 9 and (chance < 61 and agilité < 61 and ini <401):  ###1###9### Dommages Air
    if doair < 9 :
      type_rune, indicatif, done = selectRune(2,7, data, nom_item)  #PaDoAir
    if doair > 8 :
      type_rune, indicatif, done = selectRune(1,7, data, nom_item)  #DoAir
    return type_rune, indicatif, done, tenta, poid, other

  if not tacle > 1 and (chance < 61 and agilité < 61 and ini <401):  ###1###10### Tacle
    type_rune, indicatif, done = selectRune(2,13, data, nom_item) #PaTac
    return type_rune, indicatif, done, tenta, poid, other

  if not reperfeu > 4 and (chance < 61 and agilité < 61 and ini <401):  ###1###11### % Résistance Feu
    type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePerFeu
    return type_rune, indicatif, done, tenta, poid, other

  if not agilité > 46 and (chance < 61 and agilité < 61 and ini <401):  ###1###12### Agilité
    if agilité == 10 or (agilité > 17 and agilité < 21) or (agilité > 27 and agilité < 31) or (agilité > 37 and agilité < 41) :
      type_rune, indicatif, done = selectRune(3,3, data, nom_item) #RaAge
    if agilité < 10 or (agilité > 10 and agilité < 18) or (agilité > 20 and agilité < 28) or (agilité > 30 and agilité < 38) or (agilité > 40) :
      type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaAge
    return type_rune, indicatif, done, tenta, poid, other

  if not reperneutre > 5 and (chance < 61 and agilité < 61 and ini <401):  ###2###1### % Résistance Neutre
    type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerNeutre
    return type_rune, indicatif, done, tenta, poid, other

  if not  (ini > 359 and ini < 401) and (chance < 61 and agilité < 61 ):  ###2###2### Inititive
    if ini < 401 :
      type_rune, indicatif, done = selectRune(2,9, data, nom_item)
    if ini > 400 :
      if agilité < 61 :
        type_rune, indicatif, done = selectRune(1,3, data, nom_item)
      elif vita < 246 :
        type_rune, indicatif, done = selectRune(1,1, data, nom_item)
      elif chance < 61 :
        type_rune, indicatif, done = selectRune(1,2, data, nom_item)
      elif agilité > 59 and chance > 59 and vita > 245 :
        type_rune, indicatif, other_rune = selectRune5('refeu') 
    return type_rune, indicatif, done, tenta, poid, other

  if not sagesse > 34 and (chance < 61 and agilité < 61 and ini <401):  ###2###3### Sagesse
    type_rune, indicatif, done = selectRune(2,4, data, nom_item)
    return type_rune, indicatif, done, tenta, poid, other

  if not (doair > 10 and doair < 13) and (chance < 61 and agilité < 61 and ini <401):  ###2###4### Dommages Air
    type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoAir
    return type_rune, indicatif, done, tenta, poid, other

  if not reperfeu > 6 and (chance < 61 and agilité < 61 and ini <401):  ###2###5### % Résistance Feu
    type_rune, indicatif, done = selectRune(1,12, data, nom_item) #RePerFeu
    return type_rune, indicatif, done, tenta, poid, other

  if not tacle> 2 and (chance < 61 and agilité < 61 and ini <401):  ###2###6### Tacle
    type_rune, indicatif, done = selectRune(1,13, data, nom_item) #Tac
    return type_rune, indicatif, done, tenta, poid, other

  if not (agilité > 55 and agilité < 61) and (chance < 61):
    if (agilité > 46 and agilité < 53) : ###2###7### agilité
      type_rune, indicatif, done = selectRune(3,3, data, nom_item) #RaAge
    if (agilité > 52  and agilité < 61):
      type_rune, indicatif, done = selectRune(2,3, data, nom_item) #PaAge
    if agilité > 60 :
      if ini < 391 :
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #Ini
      elif chance < 60 : 
        type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Cha
      elif vita < 246 :
        type_rune, indicatif, done = selectRune(1,1, data, nom_item) #vi
      else :
        type_rune, indicatif, other_rune = selectRune5('refeu')
    return type_rune, indicatif, done, tenta, poid, other

  if not (chance > 55 and chance < 61)  and (agilité < 61): 
    if (chance > 46 and chance < 53) : ###2###8### Chance
      type_rune, indicatif, done = selectRune(3,2, data, nom_item) #RaCha
    if (chance > 52 and chance < 61):
      type_rune, indicatif, done = selectRune(2,2, data, nom_item) #PaCha
    if chance > 60 :
      if ini < 391 :
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #Ini
      elif agilité < 60 : 
        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Age
      elif vita < 246 :
        type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vi
      else :
        type_rune, indicatif, other_rune = selectRune5('refeu')          
    return type_rune, indicatif, done, tenta, poid, other

  if not (vita > 239 and vita < 251) and (chance < 61 and agilité < 61 and ini <401):  ###2###9### Vitalité
    if (vita > 199 and  vita < 206) :
      type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
    if (vita > 205 and vita < 240) :
      type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
    if (vita > 250 and vita < 256) :
      if chance < 60 :
        type_rune, indicatif, done = selectRune(1,2, data, nom_item) #Cha
      elif agilité < 60 :
        type_rune, indicatif, done = selectRune(1,3, data, nom_item) #Age
      elif ini < 391 :
        type_rune, indicatif, done = selectRune(1,9, data, nom_item) #Ini
      else:
        type_rune, indicatif, other_rune = selectRune5('refeu')
    if vita > 255 :
      type_rune, indicatif, other_rune = selectRune5('refeu')
    return type_rune, indicatif, done, tenta, poid, other

  if not (doeau > 10 and doeau < 13) and (chance < 61 and agilité < 61 and ini <401):  ###2###10### Dommages Eau
    type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoEau
    return type_rune, indicatif, done, tenta, poid, other             

  if not (tacle > 3 and tacle < 6) and (chance < 61 and agilité < 61 and ini <401):  ###2###11### Tacle
    type_rune, indicatif, done = selectRune(1,13, data, nom_item) #Tac
    return type_rune, indicatif, done, tenta, poid, other

  if not reperterre > 6 and (chance < 61 and agilité < 61 and ini <401):  ###2###12### % Résistance Terre
    type_rune, indicatif, done = selectRune(1,11, data, nom_item) #RePerTerre
    return type_rune, indicatif, done, tenta, poid, other

  if not reperneutre > 6 and (chance < 61 and agilité < 61 and ini <401):  ###2###13### % Résistance Neutre
    type_rune, indicatif, done = selectRune(1,10, data, nom_item) #RePerNeutre
    return type_rune, indicatif, done, tenta, poid, other          

  if not  (ini > 389 and ini < 401) and (chance < 61 and agilité < 61 ):  ###2###2### Inititive
    if ini < 401 :
      type_rune, indicatif, done = selectRune(2,9, data, nom_item)
    if ini > 400 :
      if agilité < 61 :
        type_rune, indicatif, done = selectRune(1,3, data, nom_item)
      elif vita < 246 :
        type_rune, indicatif, done = selectRune(1,1, data, nom_item)
      elif chance < 61 :
        type_rune, indicatif, done = selectRune(1,2, data, nom_item)
      elif agilité > 59 and chance > 59 and vita > 245 :
        type_rune, indicatif, other_rune = selectRune5('refeu') 
    return type_rune, indicatif, done, tenta, poid, other 
  
  if near_perf and poid >= min:
    type_rune = 5
    if not (doair > 11 and doair < 13) and (chance < 61 and agilité < 61 and ini <401) and poid >= type_rune:  ###2###4### Dommages Air
      type_rune, indicatif, done = selectRune(1,7, data, nom_item) #DoAir
      return type_rune, indicatif, done, tenta, poid, other
    type_rune = 5
    if not (doeau > 11 and doeau < 13) and (chance < 61 and agilité < 61 and ini <401) and poid >= type_rune:  ###2###10### Dommages Eau
      type_rune, indicatif, done = selectRune(1,6, data, nom_item) #DoEau
      return type_rune, indicatif, done, tenta, poid, other 
    type_rune = 4
    if not (tacle > 4 and tacle < 6) and (chance < 61 and agilité < 61 and ini <401) and poid >= type_rune:  ###2###11### Tacle
      type_rune, indicatif, done = selectRune(1,13, data, nom_item) #Tac
      return type_rune, indicatif, done, tenta, poid, other
    if mode == "reperair":
      type_rune = 6
      scroll('down')
      list_1 = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
      scroll('up')
      if list_1[0].find('Résistance') != -1 or  list_1[0].find('Résistance') != -1 : 
        if list_1[0].find('PM') != -1 or  list_1[0].find('PM') != -1 : 
          other = OtherItem(nombre_item)
          return type_rune, indicatif, done, tenta, poid, other
        else :
          type_rune, indicatif, other_rune = selectRune5('pm')
          exo = "1% Résistance Air"
          suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data) 
          return type_rune, indicatif, done, tenta, poid, other
      elif poid >= type_rune :
        type_rune, indicatif, other_rune = selectRune5('reperair')
        return type_rune, indicatif, done, tenta, poid, other
    if mode == "overvita":
      if poid >= min or vita > 300:
        type_rune = 10 
        if vita < 256 and poid >= type_rune:
          type_rune, indicatif, done = selectRune(3,1, data, nom_item) #RaVi
        type_rune = 3
        if vita < 291 and poid >= type_rune:
          type_rune, indicatif, done = selectRune(2,1, data, nom_item) #PaVi
        type_rune = 1
        if vita < 301 and poid >= type_rune:
          type_rune, indicatif, done = selectRune(1,1, data, nom_item) #Vi
        return type_rune, indicatif, done, tenta, poid, other
      else:
          type_rune, indicatif, other_rune = selectRune5('pm')
          exo = ""
          suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data) 
          return type_rune, indicatif, done, tenta, poid, other
  if near_perf :
    type_rune, indicatif, other_rune = selectRune5('pm')
    exo = ""
    suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data) 
    return type_rune, indicatif, done, tenta, poid, other

    

