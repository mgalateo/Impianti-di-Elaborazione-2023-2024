import glob
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import csv

baseURL="vmstat/"

# Crea una lista di percorsi per tutti i file csv nella cartella /Dati
csv_files = glob.glob(os.path.join(baseURL, "*"))
# Ordina la lista in ordine alfabetico
csv_files.sort(key=lambda file: os.path.basename(file))

for csv_file in csv_files:
    nameFile=csv_file.replace(baseURL, "")
    # Leggi il testo
    with open(csv_file) as f:
        text = f.read()

    # Dividi il testo in righe
    lines = text.split("\n")

    # Crea una lista di liste per rappresentare il file CSV
    csv_data = []
    for line in lines:
        csv_row = line.split()
        csv_data.append(csv_row)

    # Scrivi il file CSV
    with open("vmstatCSV/"+nameFile, "w") as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
