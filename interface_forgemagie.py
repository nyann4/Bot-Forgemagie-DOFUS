from tkinter import *
import numpy as np
import time
import json
import time
from pathlib import Path

def aftering(path_pui_item):
    start_function(path_pui_item)
    ws.after(1000, aftering, path_pui_item)

def start_function(path_pui_item):
    try :
        with open (path_pui_item) as my_file:
            data_pui = json.load(my_file)
        label_poid.config(text='poid actuel :'+str(data_pui['poid_actuel']))
        label_pa.config(text='nombre de pa :'+str(data_pui['nombre_pa']))
        label_po.config(text='nombre de po :'+str(data_pui['nombre_po']))
    except json.JSONDecodeError:
        time.sleep(0.5)
ws = Tk()
ws.title('Ressources')
ws.geometry('200x300+10+550')
ws.config(bg='#5f734c')
ws.resizable(False, False)
ws.attributes('-topmost', True)
ws.attributes('-alpha', 0.8)


under1_root_path = Path("..").resolve()
path_pui_item = under1_root_path / "pui_item/pui.json"

with open (path_pui_item) as my_file:
    data_pui = json.load(my_file)
tableau_1 = Frame(ws)
tableau_1.config(bg='#5f734c')

label_poid = Label(tableau_1,text=data_pui["poid_actuel"],font=(15),padx=4,pady=3,bg='#5f734c')
label_pa = Label(tableau_1,text=data_pui["nombre_pa"],font=(15),padx=4,pady=3,bg='#5f734c')
label_po = Label(tableau_1,text=data_pui["nombre_po"],font=(15),padx=4,pady=3,bg='#5f734c')
label_poid.pack(expand=True)
label_pa.pack(expand=True)
label_po.pack(expand=True)
tableau_1.pack(side='left', expand='True')
ws.update()
ws.after(1000, aftering, path_pui_item)

ws.mainloop()