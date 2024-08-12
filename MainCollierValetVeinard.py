from screen import *
from CalculCollierValetVeinard import *
from pynput.keyboard import Listener, Key
import time
import signal
import os
from Macro1 import *
from MainScreen import *
from Reconnect import *
from Launcher import reset_raccourci_page
import json
from pathlib import Path

def on_release(key): #fonction qui stop le programme
    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)


def MainCollierValetVeinard(poid, nombre_ligne_item, mode, double_exo, useless_stat, under1_root_path, path_dict_item, min):
    carac_position = [0.2, 1.0, 3.0, 0.0, 100.0, 51.0, 5.0, 3.0, 6.0, 6.0, 7.0, 2.0] #liste de Pui par unité par ligne
    X, done, type_rune, other_rune=  0, False, 0, False # affection des valeurs a chaque lancement du programme
    highest_rune, second_highest, reliquat_reading = 100, 51, False
    tenta, tenta_plus, other = 0, 0, False
    path_pui_item = under1_root_path / "pui_item/pui.json"
    while(done != True): #Boucle principale
        start = time.time()
        print('### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###')
        time.sleep(0.85) #timer minimal pour qu'aucune erreur de pui ne soit produite
        list_value, pui = get_stats(nombre_ligne_item, carac_position) #prend environ 0.39 seconde
        if X == 0:
            with open(path_pui_item, encoding='utf-8') as outfile: #pui_item
                data_pui =json.load(outfile)
            data_pui['pui'] = pui
            data_pui["nombre_pa"] = 0
            data_pui["nombre_po"] = 0
            with open(path_pui_item, "w", encoding= "utf-8") as outfile: #pui_item
                json.dump(data_pui, outfile)
        if X != 0 :
            with open(path_pui_item, encoding='utf-8') as outfile: #pui_item
                data_pui =json.load(outfile)
            old_stat = data_pui['pui']
            diff = float((sum(pui) - sum(old_stat)))
            diff_rune_indic = pui[indicatif] - old_stat[indicatif] 
            if ((old_stat[4] - pui[4]) == 100) or ((old_stat[5] - pui[5]) == 51) or poid >= min:
                reliquat_reading, lag = reliquat_true(X, path_dict_item)
                if lag or old_stat == pui:
                    list_value, pui = get_stats(nombre_ligne_item, carac_position)
                    diff = float((sum(pui) - sum(old_stat)))
                    diff_rune_indic = pui[indicatif] - old_stat[indicatif] 
                if reliquat_reading:                                                    #calcul la différence de poid si du reliquat a était enlevé ou ajouté
                    poid = calcul_de_pui(diff, reliquat_reading, poid, type_rune, diff_rune_indic, highest_rune, second_highest, other)
                else :
                    if other_rune:
                        poid_sup = calcul_poid_exo(nombre_ligne_item, data)
                        poid += poid_sup
            if poid < min:
                poid = 0
            other = False
            data_pui["poid_actuel"] = poid
            if type_rune == 100 :
                data_pui["nombre_pa"]+=1
            if type_rune == 51 :
                data_pui["nombre_po"]+=1

            data_pui['pui'] = pui
            with open(path_pui_item, "w", encoding= "utf-8") as outfile: #pui_item
                json.dump(data_pui, outfile)

        type_rune, indicatif, done, tenta, poid, other, other_rune = UpStats2(list_value, poid, nombre_item, nombre_ligne_item, tenta, nom_item, mode, double_exo, carac_position)
        end = time.time()
        if X >0 :
            print('runes :', X, 'time :', end - start, '############# diff_rune_indic :', diff_rune_indic,"différence :", diff ,'poid actuel :', poid, 'type_rune :' ,type_rune, "reliquat :", reliquat_reading)
        X += 1
        print('### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###')

time.sleep(0.2)
print("entrez le poid actuel de l'item :")
poid = float(input())
print("entrez le nombre d'item :")
nombre_item = int(input())
print("entrez le mode : 1 pour RePerAir // 2 pour OverVita // 3 pour DoSort")
exo = int(input())
print("entrez 1 pour double exo 0 pour exo normaux")
double_exo =int(input())
nom_item = "Collier du Valet Veinard"

under1_root_path = Path("..").resolve()
path_dict_item = under1_root_path / "DictionnaireItem/item.json"
with open(path_dict_item, encoding='utf-8') as outfile:
    data =json.load(outfile)
data['reliquat']['reliquat'] ="aaaa"
with open(path_dict_item, "w", encoding= "utf-8") as outfile: 
    json.dump(data, outfile, ensure_ascii=False)

path_pui_item = under1_root_path / "pui_item/pui.json"
with open(path_pui_item, encoding='utf-8') as outfile:
    data2 =json.load(outfile)
data2['last_rune']['pos'] = [100,100]
data2['last_rune']['last_rune'] = "nothing"
with open(path_pui_item, "w", encoding= "utf-8") as outfile: #pui_item
    json.dump(data2, outfile, ensure_ascii=False)

nombre_ligne_item = data[nom_item]['nombre_ligne_item']
print('nombre_ligne', nombre_ligne_item)
useless_stat = data[nom_item]['useless_stat']
print('start')

if exo == 1:
    mode = "reperair"
    min = 6
if exo == 2:
    mode = "overvita"
    min = 1
if exo == 3:
    mode = "dosort"
    min = 15

time.sleep(2)
click_categorie_item(1390, 133) #clic sur la bonne catégorie d'item
start_fm(1339, 828 ,nom_item) #tape le nom de l'item dans la barre de recherche 
FirstItem() # selectionne le premier item
time.sleep(1)

reset_raccourci_page() #remet a la normale la page de raccourcis  et met a la page 2 la page de raccourcis
with Listener(on_press=lambda k: None, on_release=on_release) as listener:
    MainCollierValetVeinard(poid, nombre_ligne_item, mode, double_exo, useless_stat, under1_root_path, path_dict_item, min) #lancement du main dans un listener pour pouvoir le stoper a la pression d'une touche a tout moment
    listener.stop()