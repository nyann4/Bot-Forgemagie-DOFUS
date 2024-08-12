from screen import screenValues
from CalculAnneauTamie import UpStat3
from pynput.keyboard import Listener, Key
import time
import signal
import os
from MainScreen import *
from Launcher import *
from Reconnect import *
import json

def on_release(key): #fonction qui stop le programme
    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

def get_stats(nombre_ligne_item, carac_position):
    list_value = screenValues(760, 341, 200, 40*nombre_ligne_item, 1)   #Screen des lignes de caractéristiques a modifiée
    list_value = parsing(list_value) 
    print("stats", list_value)
    pui = calcul_poids_ligne(carac_position, list_value, nombre_ligne_item)
    return list_value, pui

def MainAnneauTamie(poid, nom_item):
    carac_position = [0.2, 1.0, 3.0, 51.0, 5.0, 4.0, 7.0] #liste de Pui par unité par ligne
    X, done, type_rune, compteur_erreur=  0, False, 0, 0 # affection des valeurs a chaque lancement du programme
    error, highest_rune, second_highest = True, 51, 1000
    tenta, tenta_plus = 0 , 0
    nombre_ligne_item = 7
    while(done != True): #Boucle principale
        pui = []
        time.sleep(0.7) #timer minimal pour qu'aucune erreur de pui ne soit produite
        list_value, pui = get_stats(nombre_ligne_item, carac_position) #prend environ 0.39 seconde
        if X == 0 or error == True:
            with open(path, encoding='utf-8') as outfile: #pui_item
                data_pui =json.load(outfile)
            data_pui['pui'] = pui
            with open(path, "w", encoding= "utf-8") as outfile: #pui_item
                json.dump(data_pui, outfile)
                error = False
        if X != 0 :
            with open(path, encoding='utf-8') as outfile: #pui_item
                data_pui =json.load(outfile)
            old_stat = data_pui['pui']
            diff = float((sum(pui) - sum(old_stat)))
            diff_rune_indic = pui[indicatif] - old_stat[indicatif] 
            if ((old_stat[4] - pui[4]) == 51) or poid > 2.9:
                reliquat_reading, lag = reliquat_true()
                poid = calcul_de_pui(diff, reliquat_reading, poid, type_rune, diff_rune_indic, highest_rune, second_highest)
            if poid == -1000 :
                compteur_erreur +=1
                error = True
                poid = 0

            data_pui['pui'] = pui
            with open(path, "w", encoding= "utf-8") as outfile: #pui_item
                json.dump(data_pui, outfile)
        A = int(list_value[0])
        time.sleep(0.10)
        if poid > 0 and A > 339:
            over = 1
        else :
            over = 0
        type_rune, indicatif, done, tenta, tenta_plus, over = UpStat3(list_value, poid, nombre_item, tenta, tenta_plus, pui, nom_item, nombre_ligne_item, over)

        X += 1
        count = 1
        print("nombre de runes :" ,X , "nombre de tenta :", tenta , "tenta très bon jet :" , tenta_plus)
        if X > 31000 :
            print("nombre d'erreur = " ,compteur_erreur)
            t = time.localtime()
            print("time.asctime(t): %s " % time.asctime(t))
            print("nombre de runes :" ,X , "nombre de tenta :", tenta , "tenta très bon jet :" , tenta_plus)
            return True

time.sleep(0.2)
print("entrez le poid actuel de l'item :")
poid = float(input())
print("entrez le nombre d'item :")
nombre_item = int(input())
nom_item = "Anneau Tamie"
print('start')
path = "C:\\Users\\yannf\\OneDrive\\SWSetup\\Bureau\\PROJET0\\CODE\\all_codes\\DictionnaireItem\\item.json"
with open(path, encoding='utf-8') as outfile:
    data =json.load(outfile)
nombre_ligne_item = data[nom_item]['nombre_ligne_item']
useless_stat = data[nom_item]['useless_stat']
print('start')
time.sleep(2.5)

click_categorie_item(1390, 133) #clic sur la bonne catégorie d'item
start_fm(1339, 828 ,nom_item) #tape le nom de l'item dans la barre de recherche 
FirstItem() # selectionne le premier item
time.sleep(1)
reset_raccourci_page() #remet a la normale la page de raccourcis  et met a la page 2 la page de raccourcis

with Listener(on_press=lambda k: None, on_release=on_release) as listener:
    MainAnneauTamie(poid, nom_item) #lancement du main dans un listener pour pouvoir le stoper a la pression d'une touche a tout moment
    listener.stop()