from tkinter import E
import pyautogui
import keyboard
import time
from Macro1 import *
from MainScreen import *
from screen import screenValues
import re

def start_fm(x, y ,Item):
    pyautogui.moveTo(x, y, duration = 0.2)
    pyautogui.click(clicks=3)
    pyautogui.write(Item)

def Reset_stand(item, x , y, type_atelier):
    pyautogui.moveTo(x, y ,duration=0.25)
    time.sleep(0.5)                             
    pyautogui.click(clicks=1)
    if type_atelier == "jaillomage":
        pyautogui.moveTo(829, 643 ,duration=0.25) #bonta 639 566
    elif type_atelier == "cordomage":
        pyautogui.moveTo(1101, 726 ,duration=0.25)
    elif type_atelier == "costumage": 
        pyautogui.moveTo(925, 273 ,duration=0.25)
    time.sleep(2)
    pyautogui.click(clicks=1)
    time.sleep(1.5)
    pyautogui.moveTo(1390, 133, duration=0.5)
    pyautogui.click(clicks=1) #clic sur la bonne catégorie d'item
    time.sleep(1)       
    start_fm(1339, 828 , item)
    time.sleep(0.5)

def click_categorie_item(x,y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click(clicks=1) #clic sur la bonne catégorie d'item
    time.sleep(1)
def selectItem(item):
    pyautogui.moveTo(1339, 828, duration = 0.25)
    pyautogui.click(clicks=3)
    time.sleep(0.5)
    pyautogui.write(item)
    pyautogui.moveTo(1299, 216, duration=0.5)
    pyautogui.rightClick()
    pyautogui.moveTo(1360, 397, duration=0.25)
    pyautogui.moveTo(1174, 397, duration=0.25)
    pyautogui.click(clicks=1)
    time.sleep(0.3)

def verify_useless_rune(word, nombre_ligne_item, useless_stats):
    malus = 0
    for n in word :
        for i in range(nombre_ligne_item):
            horizontal_rune_pos = np.arange(336, 856, 40)
            column = horizontal_rune_pos[i-1]   
            list_1 = screen(760, column, 250, 37, 1) #screen a la ligne de la statistiques
            string = list_1[0]
            if string.find(n) != -1 : # si le mot prospection est présent, masque la ligne
                if column == 816 and nombre_ligne_item < 13: #dernière ligne
                    pass
                else :
                    pyautogui.click(642,column +18, duration=0.40, clicks=2)
                    time.sleep(0.1)
                    malus +=1
            if malus == useless_stats :
                break
    if nombre_ligne_item < 13:
        nombre_ligne_item -=malus
    return nombre_ligne_item 

def calcul_de_pui(diff, reliquat_reading, poid, type_rune, diff_rune_indic, highest_rune, second_highest, other):
    if diff == 0 and reliquat_reading == True :
        poid = poid - type_rune
    if diff != 0 and reliquat_reading == True :
        if diff < 0 :
            if  abs(diff) > type_rune :
                if type_rune == 90 or type_rune == 100 : #correction du calcul dans le cas ou la rune passé est un Pa ou PM pas présent sur l'item
                    poid = poid - (type_rune - abs(diff))
                elif diff_rune_indic > 0:
                    poid = poid + abs(diff)
                else:
                    poid = poid + (abs(diff) - type_rune)
            elif abs(diff) <= type_rune :
                if type_rune == 90 or type_rune == 100 : #correction du calcul dans le cas ou la rune passé est un Pa ou PM pas présent sur l'item
                    poid = poid - (type_rune - abs(diff))
                elif diff_rune_indic > 0:
                    poid = poid + abs(diff)
                elif diff_rune_indic == 0:
                    poid = poid - (type_rune - abs(diff))
                         
        if diff > 0 :
            if abs(round((diff),2)) < type_rune :
                poid = poid - diff
            if abs(round((diff),2)) >= type_rune:
                poid = poid - type_rune
    poid = float("{:.1f}".format(poid))

    if poid < 0 or other:
        poid = 0
    if poid >= highest_rune:
        poid =0

    return poid, other

def calcul_poid_exo(nombre_ligne_item, data):
    import re
    last_line = screenValues(760, 341+40*nombre_ligne_item, 200, 40, 1)
    if last_line[0]!= "\x0c":
        number = re.sub("[^0-9]","", last_line[0])
        rune = clean_string(last_line)
        poid_sup= int(data['dict_poid_ligne'][rune[0]])*int(number[0])
    else :
        poid_sup = 0
    print('poid ajouter :', poid_sup)
    return poid_sup

def parsing(list, nombre_ligne_item):
    import re
    list = list[0].splitlines() # decoupage en élements indépendant dans une liste  
    iter = 0 
    if nombre_ligne_item > 12:
        for n,m in enumerate(list) :
            if m.find('-') != -1:
                list.pop(n)
    while '' in list: #suppression des espace vide 
        list.remove('')
    while iter < len(list) : #transformation de chaque élément de la liste en int (seulement des nombre) 
        list[iter] = re.sub("[^0-9]","", list[iter])
        if list[iter] == '':
            list[iter] =0
        iter += 1
    return list

def clean_string(list_value):
    import re
    list_value[0] = re.sub("[0-9]","", list_value[0])
    list_value[0] = re.sub("\n","", list_value[0])
    list_value[0] = re.sub("\x0c","", list_value[0])
    if list_value[0] != "":
        while list_value[0][-1] == ' ':
            list_value[0] = list_value[0][:-1]
        while list_value[0][0] == ' ':
            list_value[0] = list_value[0][1:]
    return list_value

def calcul_poids_ligne(carac_position, list, nombre_ligne_item):
    w =0
    pui = []
    for n in range(nombre_ligne_item):
        pui.append(0)
    while w < len(carac_position) : # creation d'une nouvelle liste "pui" qui a pour valeurs le poid de chacune des statistiques de l'item 
        stats = carac_position[w]*int(list[w])
        stats = round(stats, 5)
        pui[w] = stats
        w += 1
    return pui

def find_black_px(X):
    from PIL import Image
    from pathlib import Path
    # start = time.time()
    if X < 26:
        rune = screenValues(274, 195, 1, 715, 1)
        w, y = 712, 712
    else :
        rune = screenValues(274, 767, 1, 140, 1)
        w, y = 137, 137
    end = time.time()
    root_path = Path(".").resolve()
    path = root_path / "screen modifier/screen_0.png"
    img = Image.open(path)
    img = img.convert('RGB')
    x = 0
    color = img.getpixel((x,y))
    while color == (0,0,0):
        y-=4
        color = img.getpixel((x,y))
    count = 0
    while count !=2 :
        if color == (0,0,0):
            count +=1
        y-=1
        color = img.getpixel((x,y))
        if count != 0 and color != (0,0,0):
            count = 0
    y+=-3
    # print(x, y)
    y = w-y
    high = y
    if high > 140 :
        high =140
    rune = screen(292, 907-y, 285, high, 1)
    end =time.time()
    # print(rune)
    # print(end-start)
    return rune 

def reliquat_true(X, path_dict_item):
    import json
    from pathlib import Path
    with open(path_dict_item, encoding='utf-8') as outfile: #dict item
        data =json.load(outfile)
    last_reliquat = data['reliquat']['reliquat']
    time.sleep(0.65)
    history = screenValues(290, 802, 285, 95, 1)
    rune =find_black_px(X)
    new_string = rune[0][:-2]
    count = 0
    lag = False
    print('new_history', history)
    print('preview_history', last_reliquat)
    if X > 1:
        while last_reliquat[0][-35:] == history[0][-35:]:
            print('lag error reliquat')
            lag = True
            time.sleep(0.4)
            list1 = screenValues(290, 802, 285, 95, 1)
            rune = list1[0]
            new_string = rune[:-2]
            count +=1
            if count > 3:
                break
    if new_string.find("reli") == -1 :
        reliquat_reading = False
    if new_string.find("reli") != -1:
        reliquat_reading = True
    data['reliquat']['reliquat'] = history
    with open(path_dict_item, "w", encoding= "utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)
    return reliquat_reading, lag

def takeScreen(posX, posY, pixelX, pixelY):
   import pyautogui 
   screen = pyautogui.screenshot(region=(posX, posY, pixelX, pixelY))
   return screen


def get_stats(nombre_ligne_item, carac_position):
    time.sleep(0.1)
    from pathlib import Path
    from PIL import Image
    list_value = screenValues(766, 345, 200, 40*nombre_ligne_item, 1)
    print('first liste', list_value)
    print(list_value)   #Screen des lignes de caractéristiques a modifiée
    list_value = parsing(list_value,nombre_ligne_item) 
    print("stats", list_value)
    start = time.time()
    img = takeScreen(977, 582, 1, 1)
    img = img.convert('RGB')
    color = img.getpixel((0,0))
    end = time.time()
    print('temps screen 1 pixel', end-start)
    if color != (0,0,0):
        pyautogui.click(919,582)
        time.sleep(1.5)
        list_value, pui = get_stats(nombre_ligne_item, carac_position)
    pui = calcul_poids_ligne(carac_position, list_value, nombre_ligne_item)
    print('balise B')
    return list_value, pui

def suivis_value(list_value, tenta,tenta_plus, pui, nom_item, exo, data):
    max_poid = data[nom_item]['max_poid']
    list_value.insert(0, "tenta = {}    ".format(tenta))
    list_value.insert(0, "tenta_plus ={}    ".format(tenta_plus))
    list_value.append(exo)
    list_value.append(str(str(round(((sum(pui))/(max_poid)*100),2))+ "%"))
    list_value.append("poid actuel :{:.1f}".format(sum(pui)))
    list_value.append(('max :'+str(max_poid)))
    list_value.append('\n')
    print('a noter' ,list_value)
    if tenta == 1 :
        with open('suivis_tenta_{}.txt'.format(nom_item), 'a') as filehandle: #ecriture du jet avant la première rune
            list_value.insert(0,'\n')
            filehandle.write(" ".join(str(item) for item in (list_value)))
    else :
        with open('suivis_tenta_{}.txt'.format(nom_item), 'a') as filehandle: #ecriture du jet avant la première rune
            filehandle.write(" ".join(str(item) for item in (list_value)))

def suivis_more_value(list_value, tenta, pui, nom_item, exo, data, value, tenta_po, nombre_ligne_item):
    docrit_screen = screen(750, (340+40*nombre_ligne_item), 200, 40, 2)
    number = re.sub("[^0-9]","", docrit_screen[0])
    docrit_screen = clean_string(docrit_screen)
    try:
        print('rune a chercher dans le dictionnaire',docrit_screen[0])
        poid = int(data['dict_poid_ligne'][docrit_screen[0]])*int(number)
    except:
        poid = 0
    max_poid = data[nom_item]['max_poid']
    list_value.insert(0, f"tenta = {tenta}    ")
    list_value.append(f'|tenta_po ={tenta_po}')
    list_value.append(('|'+str(exo)+'|'))
    list_value.append(str(str(round(((sum(pui)+poid)/(max_poid)*100),2))+ "%"))
    list_value.append("| poid actuel :{:.1f}  |".format(sum(pui)+poid))
    list_value.append(('max :'+str(max_poid)))
    list_value.append(value)
    list_value.append('\n')
    if tenta == 1 :
        with open('suivis_more_{}.txt'.format(nom_item), 'a') as filehandle: #ecriture du jet avant la première rune
            list_value.insert(0,'\n')
            filehandle.write(" ".join(str(item) for item in (list_value)))
    else :
        with open('suivis_more_{}.txt'.format(nom_item), 'a') as filehandle: #ecriture du jet avant la première rune
            filehandle.write(" ".join(str(item) for item in (list_value)))

def go_to_chest5():
    pyautogui.click(726, 263, duration=0.3) #clic sur lescalier 1 
    time.sleep(3.5)
    pyautogui.click(737, 392, duration=0.3)# clic sur lescalier 2 
    time.sleep(2)
    pyautogui.click(1208, 707, duration=0.3) #clic sur le coffre 
    time.sleep(0.5)
    pyautogui.click(1257, 744, duration=0.3) #clic sur ouvrir
    time.sleep(3)

def go_to_chest1():
    pyautogui.click(907, 730, duration=0.3) #clic sur lescalier1
    time.sleep(3.5)
    pyautogui.click(1080, 553, duration=0.3) #clic sur le coffre 
    time.sleep(0.5)
    pyautogui.click(1137, 594, duration=0.3) #clic sur ouvrir
    time.sleep(3)

def transfert_rune(preset, list_name_rune_item, list_quantity):
    if preset == 1 :
        time.sleep(0.25)
        pyautogui.click(1582, 93, duration=0.3)# ferme l'atelier
        time.sleep(2)
        pyautogui.click(1246, 990, duration=0.3)
        time.sleep(0.5)
    pyautogui.click(990, 1031, clicks = 2 , duration=0.3) #clic sur la potion de foyer 
    time.sleep(2)
    go_to_chest1()
    x = 0
    result_quantity = []
    while x < len(list_name_rune_item) :
        time.sleep(0.8)
        quantity = list_quantity[x]
        pyautogui.click(494, 857, duration=0.3) #clic sur la barre de recherche
        time.sleep(0.5)
        pyautogui.write(list_name_rune_item[0]) # ecris la rune dans la barre de recherche
        time.sleep(0.2)
        list_value  = screenValues(317, 211, 40, 12, 1)
        if int(list_value[0]) < quantity :
            result_quantity.append(str(list_name_rune_item[x]+'  :' +list_value[0]))
        else :
            result_quantity.append(str(list_name_rune_item[x]+'  :' +0))
        pyautogui.dragTo(1267, 242 ,0.5,button='left')
        x += 1
    # time.sleep(3)
    # pyautogui.click(1551, 118, duration=0.3) #ferme coffre 
    # time.sleep(1)
    # pyautogui.click(812, 990, clicks= 2, duration=0.3) # clic sur la potion de rappel
    # time.sleep(4)
    # pyautogui.click(929, 948, duration=0.3) # change de map
    # time.sleep(5.5)
    # pyautogui.click(1257, 503, duration=0.3) #clic sur l'entrée de l'atelier
    # time.sleep(3.5)
    # pyautogui.click(820, 636, duration=0.3)  #clic sur l'atelier
    # time.sleep(2)
    # pyautogui.click(1246, 1031, duration=0.3)
    time.sleep(0.5) 
# time.sleep(1.5)
# find_black_px(12)