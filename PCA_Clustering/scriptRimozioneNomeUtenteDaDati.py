#Leggo i dati dal csv DataCollector01.csv

import glob
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import re

csv_files = glob.glob(os.path.join("", "*.csv"))
# Ordina la lista in ordine alfabetico
csv_files.sort(key=lambda file: os.path.basename(file))

if(len(csv_files)==0):
    print("Non ci sono file csv nella cartella corrente")
    exit()
if(len(csv_files)>1):
    print("Ci sono più file csv nella cartella corrente")
    exit()

#leggo il file csv

df = pd.read_csv(csv_files[0])

df.columns = df.columns.str.replace(r'\\', '')

df.columns = df.columns.str.replace("\\", "/",)


df.columns = df.columns.map(lambda x: re.sub(r"[A-Za-z]+/", "", x))

df.columns = df.columns.str.replace("(_Total)", "",)


#creo un file csv con i dati puliti chiamato Dati.csv
df.to_csv("Dati.csv", index=False)
print("File Dati.csv creato con successo")
