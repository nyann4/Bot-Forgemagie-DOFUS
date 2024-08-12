from screen import *
from CalculAnneauAllister import *
from pynput.keyboard import Listener, Key
import time
import signal
import os
from Macro1 import *
from MainScreen import *
from Reconnect import *
from Launcher import reset_raccourci_page

def on_release(key): #fonction qui stop le programme
    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

def MainAnneauDallister(poid):
    carac_position = [0.2, 1.0, 3.0, 10.0, 30.0, 5.0, 3.0, 7.0, 2.0] #liste de Pui par unité par ligne
    X, done, type_rune, compteur_erreur=  0, False, 0, 0 # affection des valeurs a chaque lancement du programme
    error, highest_rune, second_highest = True, 30, 1000
    tenta, tenta_plus = 0 , 0
    nombre_ligne_item = 9
    while(done != True): #Boucle principale
        pui = []
        time.sleep(0.7) #timer minimal pour qu'aucune erreur de pui ne soit produite
        list_value = screenValues(767, 341, 200, 40*nombre_ligne_item, 1)   #Screen des lignes de caractéristiques a modifiée

        list_value = parsing(list_value) 

        pui = calcul_poids_ligne(carac_position, list_value, pui, w = 0)

        print("stats", list_value)

        if X == 0 or error == True:
            with open('listfile.txt', 'w') as filehandle: #ecriture du jet avant la première rune
                filehandle.writelines("%s\n" % place for place in pui)
                error = False
        if X != 0 :
            old_stat = []
            with open('listfile.txt', 'r') as filehandle: #lecture de l'ancien pui
                filecontents = filehandle.readlines()
                for line in filecontents:
                    current_place = float(line[:-1])
                    old_stat.append(current_place)
            diff = float("{:.1f}".format(sum(pui) - sum(old_stat)))
            diff_rune_indic = pui[indicatif] - old_stat[indicatif] 
            if (old_stat[4] - pui[4]) == 30 or poid > 2.9:
                reliquat_reading = reliquat_true()
                poid = calcul_de_pui(diff, reliquat_reading, poid, type_rune, diff_rune_indic, highest_rune, second_highest)

            print("                                                            poid actuel = ", poid, "différence :", diff)
            if poid < 0 :
                compteur_erreur +=1
                error = True
                poid = 0

            with open('listfile.txt', 'w') as filehandle: #ecriture du pui actuel pour faire la différence avec le nouveau pui
                filehandle.writelines("%s\n" % place for place in pui)

        time.sleep(0.10)
        type_rune, indicatif, done, tenta, tenta_plus = UpStats2(list_value, poid, nombre_item, tenta, tenta_plus, pui, nom_item, nombre_ligne_item)

        X += 1
        count = 1
        print("nombre de runes :" ,X , "nombre de tenta :", tenta , "tenta très bon jet :" , tenta_plus)
        if X > 31000 :
            print("nombre d'erreur = " ,compteur_erreur)
            t = time.localtime()
            print("time.asctime(t): %s " % time.asctime(t))
            print("nombre de runes :" ,X , "nombre de tenta :", tenta , "tenta très bon jet :" , tenta_plus)
            return True
        if X%(count*150) == 0 :
            Debug(900, 586)
            time.sleep(0.4)
            verify_useless_rune(760, 621, 'Prospection')
        if X%(count*100) == 0 :
            print("nombre d'erreur =" ,compteur_erreur, "########")
        if X%(count*150000) == 0 : 
            time.sleep(0.5)
            Reset_stand(nom_item, 1587, 91, 'jaillomage') #ferme et réouvre l'atelier
            FirstItem()
            verify_useless_rune(760, 621, 'Prospection')
            poid = 0
        if X%(count*50000) == 0:
            transfert_rune()
            FirstItem()
            # return_stand()

time.sleep(0.2)
print("entrez le poid actuel de l'item :")
poid = float(input())
print("entrez le nombre d'item :")
nombre_item = int(input())
nom_item = "anneau d'allister"
print('start')

time.sleep(2.5)

click_categorie_item(1390, 133) #clic sur la bonne catégorie d'item
start_fm(1339, 828 ,nom_item) #tape le nom de l'item dans la barre de recherche 
FirstItem() # selectionne le premier item
time.sleep(1)

verify_useless_rune(760, 621, 'Prospection') #verifie et enlève la ligne "prospection" pour que l'item n'est pas trop de ligne
reset_raccourci_page() #remet a la normale la page de raccourcis  et met a la page 2 la page de raccourcis

with Listener(on_press=lambda k: None, on_release=on_release) as listener:
    MainAnneauDallister(poid) #lancement du main dans un listener pour pouvoir le stoper a la pression d'une touche a tout moment
    listener.stop()