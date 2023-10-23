import glob
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import csv

baseURL="vmstatCSV/"

# Crea una lista di percorsi per tutti i file csv nella cartella /Dati
csv_files = glob.glob(os.path.join(baseURL, "*"))
# Ordina la lista in ordine alfabetico
csv_files.sort(key=lambda file: os.path.basename(file))
v=np.arange(0, 305,dtype=int)

for csv_file in csv_files:
    nameFile=csv_file.replace(baseURL, "")
    #elimino l'estensione
    nameFile=nameFile.replace(".csv", "")


    df = pd.read_csv(csv_file)
    df['sy'] = df['sy'].astype(int)
    df = df.reset_index()
    # Crea il grafico
    # Imposta i limiti dell'asse y
    plt.ylim([0, 100])
    plt.plot(df['sy'], linewidth=1, color='green')

    plt.xlabel("Tempo")
    plt.ylabel("sy")
    plt.title("Sy nel tempo")
    plt.grid(True)
    plt.savefig("Grafici/sy/"+nameFile+".png")
    plt.close()


    # Crea il grafico
    # Imposta i limiti dell'asse y
    plt.plot(df['libero'], linewidth=1, color='blue')

    plt.xlabel("Tempo")
    plt.ylabel("Memoria Libera")
    plt.title("Memoria libera nel tempo")
    plt.grid(True)
    plt.savefig("Grafici/memoria/"+nameFile+".png")
    plt.close()
