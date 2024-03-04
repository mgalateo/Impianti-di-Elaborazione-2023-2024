#chiedi di inserire a terminale il nome della cartella in cui si trovano i file

import glob
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def calcola_media_ogni_5_righe(valori):
    medie = []
    for i in range(0, len(valori), 5):
        media_parziale = sum(valori[i:i+5]) / 5
        medie.append(media_parziale)
    return medie

#richiedi il nome della cartella in cui si trovano i file
print("Inserisci il nome della cartella in cui si trovano i file")
cartella = input()

#controllo che la cartella esista
if os.path.isdir(cartella):
    print("La cartella esiste")
else:
    print("La cartella non esiste")
    exit()



# Crea una lista di percorsi per tutti i file csv nella cartella /Dati
txt_files = glob.glob(os.path.join(cartella+"/", "*"))
# Ordina la lista in ordine alfabetico
txt_files.sort(key=lambda file: os.path.basename(file))

#crea un dataframe vuoto
df = pd.DataFrame()




#per ogni file di testo nella cartella 
for file in txt_files:
    with open(file, 'r') as filet:
        lines = filet.readlines()

        df = pd.DataFrame()

        # Estrai solo i numeri dalle righe e crea una lista
        numbers = [int(line.split()[1]) for line in lines if 'Time:' in line]
        medie = calcola_media_ogni_5_righe(numbers) 
        #IL NOME DEL FILE E' DATO DALLA VARIABILE file ELIMINANDO IL PERCORSO
        nomeFile = os.path.basename(file)
        nome = nomeFile.replace(".txt", "")
        df[nomeFile] = medie

        #salco il dataframe in un file csv
        df.to_csv(nome+".csv", index=False)
        print("File csv creato: "+nome+".csv")




