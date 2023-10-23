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

# Crea una matrice Pandas con le colonne desiderate
results = pd.DataFrame(columns=[
    "File",
    "ctt",
    "r",
    "b",
    "swpd",
    "libero",
    "buff",
    "cache",
    "si",
    "so",
    "bi",
    "bo",
    "inn",
    "cs",
    "us",
    "sy",
    "id",
    "wa",
    "st"
    
])

for csv_file in csv_files:
    nameFile=csv_file.replace(baseURL, "")
    #elimino l'estensione
    nameFile=nameFile.replace(".csv", "")
    ctt=nameFile.split("C")[0]


    df = pd.read_csv(csv_file)
    r=df['r'].mean()
    b=df['b'].mean()
    swpd=df['swpd'].mean()
    libero=df['libero'].mean()
    buff=df['buff'].mean()
    cache=df['cache'].mean()
    si=df['si'].mean()
    so=df['so'].mean()
    bi=df['bi'].mean()
    bo=df['bo'].mean()
    inn=df['in'].mean()
    cs=df['cs'].mean()
    us=df['us'].mean()
    sy=df['sy'].mean()
    id=df['id'].mean()
    wa=df['wa'].mean()
    st=df['st'].mean()

   # Aggiungi i dati alla matrice Pandas
    results.loc[len(results)] = [
        csv_file,
        ctt,
        r,
        b,
        swpd,
        libero,
        buff,
        cache,
        si,
        so,
        bi,
        bo,
        inn,
        cs,
        us,
        sy,
        id,
        wa,
        st
    ]

#rendo ctt un intero
results['ctt'] = results['ctt'].astype(int)
results = results.sort_values(by=["ctt","File"])

tabellaMedia = pd.DataFrame(columns=[ "ctt", "r", "b", "swpd", "libero", "buff", "cache", "si", "so", "bi", "bo", "inn", "cs", "us", "sy", "id", "wa", "st"])
for i in range(0, len(results), 3):
    df1=results.iloc[i:i+3]
    ctt=results.iloc[i]['ctt']
    r=df1['r'].mean()
    b=df1['b'].mean()
    swpd=df1['swpd'].mean()
    libero=df1['libero'].mean()
    buff=df1['buff'].mean()
    cache=df1['cache'].mean()
    si=df1['si'].mean()
    so=df1['so'].mean()
    bi=df1['bi'].mean()
    bo=df1['bo'].mean()
    inn=df1['inn'].mean()
    cs=df1['cs'].mean()
    us=df1['us'].mean()
    sy=df1['sy'].mean()
    id=df1['id'].mean()
    wa=df1['wa'].mean()
    st=df1['st'].mean()
    tabellaMedia.loc[i]=[ctt, r, b, swpd, libero, buff, cache, si, so, bi, bo, inn, cs, us, sy, id, wa, st]

#salvo la tabella in un file csv
tabellaMedia.to_csv('tabellaMediaVmstat.csv', index=False)

# Crea il grafico

tabellafinale1 = pd.DataFrame(columns=["ctt", "r", "b", "swpd", "libero", "buff", "cache", "si", "so", "bi", "bo", "inn", "cs", "us", "sy", "id", "wa", "st"])
tabellafinale2 = pd.DataFrame(columns=["ctt", "r", "b", "swpd", "libero", "buff", "cache", "si", "so", "bi", "bo", "inn", "cs", "us", "sy", "id", "wa", "st"])

for i in range(0, len(tabellaMedia)):

    if tabellaMedia.iloc[i]['ctt']<=6500:
        tabellafinale1.loc[i]= tabellaMedia.iloc[i]
    if tabellaMedia.iloc[i]['ctt']>=6500:
        tabellafinale2.loc[i]= tabellaMedia.iloc[i]

# Crea il grafico
#plt.plot(tabellafinale2['ctt'], tabellafinale2['sy'],'o--', linewidth=1, color='black', label='cpu')
plt.plot(tabellafinale1['ctt'], tabellafinale1['sy'],'o-', linewidth=2, color='red', label='cpu')
plt.xlabel("CTT")
plt.ylabel("sy")
plt.title("Percentuale di utilizzo CPU per CTT")
plt.grid(True)
plt.savefig("Grafici/CPU.png")
plt.close()

# Crea il grafico
#plt.plot(tabellafinale2['ctt'], tabellafinale2['buff'],'o--', linewidth=1, color='black', label='Buffer')
plt.plot(tabellafinale1['ctt'], tabellafinale1['buff'],'o-', linewidth=2, color='green', label='Buffer')
plt.xlabel("CTT")
plt.ylabel("Buffer")
plt.title("Memoria per CTT")
plt.grid(True)
plt.savefig("Grafici/MemoriaBuffer.png")
plt.close()

# Crea il grafico
#plt.plot(tabellafinale2['ctt'], tabellafinale2['cache'],'o--', linewidth=1, color='black', label='Cache')
plt.plot(tabellafinale1['ctt'], tabellafinale1['cache'],'o-', linewidth=2, color='blue', label='Cache')
plt.xlabel("CTT")
plt.ylabel("Cache")
plt.title("Cache per CTT")
plt.grid(True)
plt.savefig("Grafici/MemoriaCache.png")
plt.close()

#plt.plot(tabellafinale2['ctt'], tabellafinale2['libero'],'o--', linewidth=1, color='black', label='Memoria Libera')
plt.plot(tabellafinale1['ctt'], tabellafinale1['libero'],'o-', linewidth=2, color='red', label='Memoria Libera')
plt.xlabel("CTT")
plt.ylabel("Memoria Libera")
plt.title("Memoria Libera per CTT")
plt.grid(True)
plt.savefig("Grafici/MemoriaLibera.png")
plt.close()





