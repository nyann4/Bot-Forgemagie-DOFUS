from screen import *
from CalculQuatreFeuille import UpStats
from pynput.keyboard import Listener, Key
import time
import signal
import os
from Macro1 import *
from MainScreen import *
from Reconnect import *
from Launcher import reset_raccourci_page

def on_release(key):
    if key == Key.end:
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

def MainQuatreFeuille(nom_item):
    carac_position = [2.0, 10.0, 4.0, 15.0]
    X, count, done = 0, 0, False
    tenta, tenta_plus = 0 , 0
    nombre_ligne_item = 4
    while(done != True):
        pui = []
        time.sleep(0.45)
        list_value = screenValues(760, 341, 100, (40*nombre_ligne_item), 1)
        list_value = parsing(list_value)
        done, tenta, tenta_plus= UpStats(list_value, nombre_item, tenta, tenta_plus, nombre_ligne_item, type_exo, nom_item)
        X += 1
        count = 1
        print("nombre de runes :" ,X, "nombre de tenta : ", tenta)
        if X > 34000 or tenta == 950:
            return True
        if X%(count*100) == 0 :
            Debug(900, 586)
            time.sleep(0.4)
        if X%(count*1500000) == 0 : 
            time.sleep(0.5)
            Reset_stand(nom_item, 1587, 91) #ferme et réouvre l'atelier
            FirstItem()

time.sleep(0.2)
print("entrez le nombre d'item :")
nombre_item = int(input())
print("entrez le nombre d'item :")
nom_item = "Quatre-feuilles"
print('1 pour exo PA / 2 pour exo PM / 3 pour exo PO')
type_exo = int(input())
print('start')
time.sleep(2.5)
click_categorie_item(1390, 133) #clic sur la bonne catégorie d'item
start_fm(1339, 828 ,nom_item) #tape le nom de l'item dans la barre de recherche 
FirstItem() # selectionne le premier item
time.sleep(1)

reset_raccourci_page() #remet a la normale la page de raccourcis  et met a la page 2 la page de raccourcis
with Listener(on_press=lambda k: None, on_release=on_release) as listener:
    MainQuatreFeuille(nom_item)
    listener.stop()