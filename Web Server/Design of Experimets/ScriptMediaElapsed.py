#salvo i nomi dei file delle cartelle contenute nella cartella Dati

import glob
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

baseURL="Dati/"

cartelle = glob.glob(os.path.join(baseURL, "*"))

#creo una dataframe con tre colonne: nome cartella,nome file e media elapsed
df = pd.DataFrame(columns=[
    "Cartella",
    "File",
    "CTT",
    "Risorsa",
    "ResponseTime",
])

for cartella in cartelle:

    csv_files = glob.glob(os.path.join(cartella, "*"))
    
    for csv_file in csv_files:
        df1= pd.read_csv(csv_file)
        mediaElapsed=df1['elapsed'].mean()
        nomecartella=cartella.replace("Dati/", "")
        #elimino tutto quello scritto dopo lo /
        nomecartella = nomecartella.split("/")[0]
        nomeFile=csv_file.replace("Dati/", "")
        nomeFile = nomeFile.replace(nomecartella, "")
        nomeFile=nomeFile.replace("/", "")
        file=nomeFile.replace(".csv", "")
        #se la prima lettera di file è S allora CTT= 1500, altrimenti se prima letera =M CTT= 3000, infine prima lettera L CTT= 4500
        if file[0]=="S":
            CTT=1500
        elif file[0]=="M":
            CTT=3000
        elif file[0]=="L":
            CTT=4500
        
        if file[1]=="S":
            Risorsa="Small"
        elif file[1]=="M":
            Risorsa="Medium"
        elif file[1]=="L":
            Risorsa="Large"


        df.loc[len(df)] = [
            nomecartella,
            nomeFile,
            CTT,
            Risorsa,
            mediaElapsed,
        ]
    
df.sort_values(by=['CTT','Risorsa'], inplace=True)

df.to_csv("MediaElapsed.csv", index=False)
        


