import pyautogui
import time
import keyboard
from MainScreen import *
import numpy as np




def selectRune4(x,y):
    pyautogui.moveTo(x, y, duration = 0.10)
    pyautogui.click(clicks=1)

def selectRune(x,y, data, nom_item):
    from pathlib import Path
    import json
    under1_root_path = Path('..').resolve()
    path_pui_item = under1_root_path / 'pui_item/pui.json'
    with open(path_pui_item, encoding='utf-8') as outfile:
        data2 =json.load(outfile)
    last_rune_pos = data2['last_rune']["pos"]
    horizontal_rune_pos = np.arange(356, 876, 40)
    vertical_rune_pos = np.linspace(1081, 1181, 3)
    line = vertical_rune_pos[x-1]
    column = horizontal_rune_pos[y-1]
    if not (last_rune_pos[0] == line and last_rune_pos[1] == column):
    # pyautogui.moveTo(line, column, duration = 0.18)
        time = 0.2
        print('balise1')
        keyboard.press('ctrl')
        pyautogui.click(line, column, duration = 0.20, clicks=2)
        keyboard.release('ctrl')
    else: 
        print('balise2')
        time = 0.35
    data2['last_rune']['last_rune'] = 'nothing'
    data2['last_rune']["pos"] = [int(line), int(column)]

    pyautogui.moveTo(959, 260, duration=time) #fusionner
    pyautogui.click(980, 260, duration=time, clicks=2)
    stats = data[nom_item]['list_carac'][int((column-356)/40)]
    rune = data["dict_poid_rune"][stats]

    multi = 1
    if int((line-1081)/50)+1 == 2:
        multi = 3
        stats =  "Pa " +str(stats)
    elif int((line-1081)/50)+1 == 3 :
        multi = 10
        stats =  "Ra "+ str(stats)
    type_rune = round(rune*multi)
    indicatif = int((column-356)/40)

    done = False
    data2['runes_item'][stats] -=1
    if data2['runes_item'][stats] == 0:
        done =  True
    with open(path_pui_item, "w", encoding= "utf-8") as outfile: #pui_item
        json.dump(data2, outfile, ensure_ascii=False)
    print('stats :', stats, 'rune :', rune, 'type_rune :', type_rune,"indicatif :", indicatif, "multi :", multi)
    return type_rune, indicatif, done
    

def selectRune5(word):
    from pathlib import Path
    import json
    under1_root_path = Path('..').resolve()
    path_pui_item = under1_root_path / 'pui_item/pui.json'
    with open(path_pui_item, encoding='utf-8') as outfile:
        data =json.load(outfile)
    last_rune = data["last_rune"]["last_rune"]
    data['last_rune']['pos'] = [100,100]
    duration = 0.18
    if word == 'pa':
        x = 1220
    if word == 'ini':
        x = 1040
    if word == 'refeu':
        x = 1085
    if word == 'po':
        x = 1130
    if word == 'pm':
        x = 1175
    if word == 'reperterre':
        x = 995
    if word == 'reperfeu':
        x = 950
    if word == 'reperair':
        x = 905
    if word == 'repereau':
        x = 860
    if word == 'reperneutre':
        x = 815
    y = 1030
    if word == "dosort":
        x = 995
        y = 985
    if word == "pod":
        x = 1040
        y = 985
    if word =="orbe":
        duration = 4
        x = 1175
        y = 985
    if word == "docrit":
        x =950
        y = 985
    if not last_rune == word :
        pyautogui.moveTo(x, y, duration = 0.1)
        keyboard.press('ctrl')
        time.sleep(0.12)
        pyautogui.click(clicks=3)
        time.sleep(0.12)
        keyboard.release('ctrl')
        time.sleep(0.12)
    v = 959
    w = 260                                
    pyautogui.click(v,w, duration = duration) #fusionner
    time.sleep(0.2)
    if x == 1220 : #Pa
        type_rune = 100
    if x == 1175 : #Pm
        type_rune = 90
    if x == 1130 : #Po
        type_rune = 51
    if x == 1085 : #Refeu
        type_rune = 2
    if x == 1040 and y == 1030: #Ini 
        type_rune = 1
    if x == 995 and y == 985 : #DoSort
        type_rune = 15
    if x < 996 and y == 1030 : #RePer
        type_rune = 6
    if x < 995 and y ==985:
        type_rune = 5
    if x == 1040 and y == 985 : #pod
        type_rune = 2.6
    indicatif = 0
    data['last_rune']['last_rune'] = word
    with open(path_pui_item, "w", encoding= "utf-8") as outfile: #pui_item
        json.dump(data, outfile, ensure_ascii=False)
    other_rune = True
    return type_rune, indicatif, other_rune


def CleanRune():
    pyautogui.moveTo(925, 193, duration = 0.1)
    time.sleep(0.2)
    keyboard.press('ctrl')
    time.sleep(0.2)
    pyautogui.click(clicks=3)
    keyboard.release('ctrl')

def FirstItem():
    time.sleep(0.1)
    pyautogui.moveTo(1290, 210, duration = 0.2)
    pyautogui.click(clicks=2)
    time.sleep(0.5)

def Debug(x,y) :
    time.sleep(0.1)
    x = 900
    y = 586
    pyautogui.moveTo(x, y, duration = 0.2)
    # keyboard.press('ctrl')
    pyautogui.click(clicks=2)

def start_fm(x, y ,Item):
    pyautogui.moveTo(x, y, duration = 0.2)
    pyautogui.click(clicks=3)
    pyautogui.write(Item)


def reset_pui(nombre_item, nom_item, categorie):
    if categorie == 'anneau' : 
        item_pod = 'anneau de brouce'
        position = 266
    elif categorie == 'amulette':
        item_pod = 'collier de tourthon'
        position = 192
    x = 0 
    w = 1336
    pyautogui.moveTo(1582, 91, duration = 0.2) # ferme l'atelier
    pyautogui.click(clicks=1)
    time.sleep(1)
    pyautogui.moveTo(1385, 985, duration = 0.2) #ouvre l'inventaire
    pyautogui.click(clicks=1)  
    time.sleep(2.5) 
    pyautogui.moveTo(1390, 149, duration = 0.2) # clique sur la bonne catégorie d'item
    pyautogui.click(clicks=1)
    time.sleep(1.5)
    pyautogui.moveTo(800, position, duration = 0.2) # enlève le premier anneau de l'équipement
    pyautogui.click(clicks=2)
    time.sleep(1.5) 
    start_fm(1403, 849, nom_item)
    time.sleep(0.7) #écris le nom de l'item dans la barre de recherche
    while x < nombre_item :
        while x < 5 and x < nombre_item:
            pyautogui.moveTo(w, 235, duration = 0.2) 
            pyautogui.click(clicks=2)
            time.sleep(1.1)    
            pyautogui.moveTo(800, position, duration = 0.2) # enlève le premier anneau de l'équipement
            pyautogui.click(clicks=2)
            time.sleep(1.1) 
            x += 1
            w += 60
        w = 1336 
        z = 295
        while  x >= 5 and x < 10 and x < nombre_item:
            pyautogui.moveTo(w, z, duration = 0.2) 
            pyautogui.click(clicks=2)
            time.sleep(1.1)    
            pyautogui.moveTo(800, position, duration = 0.2) # enlève le premier anneau de l'équipement
            pyautogui.click(clicks=2)
            time.sleep(1.1) 
            x += 1
            w += 60
    start_fm(1403, 849, item_pod) #ré equipe l'anneau du stuff pods
    time.sleep(0.7)
    pyautogui.moveTo(1336, 235, duration = 0.2) 
    pyautogui.click(clicks=2)
    time.sleep(1.5)   
    pyautogui.moveTo(1624, 106, duration = 0.2) # ferme l'inventaire
    pyautogui.click(clicks=1)
    time.sleep(1) 

def OtherItem(nombre_item):
    plus_five = 0
    while nombre_item > 6:
        nombre_item -= 5
        plus_five +=1
    if nombre_item < 7 :
        x = 1180 + nombre_item*60
        y = 215+ plus_five*60
        time.sleep(0.1)
        pyautogui.moveTo(x, y, duration = 0.2)
        pyautogui.click(clicks=2)
        time.sleep(0.5)
    other = True
    return other

def Scroll(direction):
    time.sleep(0.25)
    pyautogui.moveTo(900, 586, duration=0.2)
    pyautogui.click(clicks=1)
    if direction == 'up' :
        pyautogui.scroll(500)
    if direction == 'down':
        pyautogui.scroll(-500)