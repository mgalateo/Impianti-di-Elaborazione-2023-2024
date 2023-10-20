import glob
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

baseURL="Dati/"

# Crea una lista di percorsi per tutti i file csv nella cartella /Dati
csv_files = glob.glob(os.path.join(baseURL, "*"))
# Ordina la lista in ordine alfabetico
csv_files.sort(key=lambda file: os.path.basename(file))


# Crea una matrice Pandas con le colonne desiderate
results = pd.DataFrame(columns=[
    "File",
    "Duration",
    "nRichiesteTot",
    "nRichiesteOk",
    "nErrori",
    "nErroriSmall",
    "nErroriMedium",
    "nErroriLarge",
    "Throughput",
    "ResponseTime",
])


matrice= pd.DataFrame()
# Itera sulla lista di percorsi e calcola il throughput e il tempo di risposta medio per ciascun file
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    df['responseCode'] = df['responseCode'].astype(str)
    nRichiesteTot=len(df)
    durataMax=max(df['timeStamp'])
    durataMin=min(df['timeStamp'])

    duration=(durataMax-durataMin)/1000

    dfRigheOk = df[df['responseCode'] == "200"]
    nRichiesteOk = len(dfRigheOk)
    dfErrori = df[df['responseCode'] != "200"]
    nErrori = len(dfErrori)
    dfErroriSmall = dfErrori[dfErrori['label'] == "Small HTTP Request"]
    dfErroriMedium = dfErrori[dfErrori['label'] == "Medium HTTP Request"]
    dfErroriLarge = dfErrori[dfErrori['label'] == "Large HTTP Request"]
    nErroriSmall = len(dfErroriSmall)
    nErroriMedium = len(dfErroriMedium)
    nErroriLarge = len(dfErroriLarge)
    
    Throughput=nRichiesteOk/duration
    #forse dovrei escludere errori?
    responseTime2 = dfRigheOk['elapsed'].mean()

    # Aggiungi i dati alla matrice Pandas
    results.loc[len(results)] = [
        csv_file,
        duration,
        nRichiesteTot,
        nRichiesteOk,
        nErrori,
        nErroriSmall,
        nErroriMedium,
        nErroriLarge,
        Throughput,
        responseTime2,
    ]

# Salva il DataFrame in un file CSV
results.to_csv("statistiche.csv", index=False)


#SCRIPT THROUGHPUT


# Importa i dati
df = pd.read_csv("statistiche.csv")

#voglio solo label e throughput
df = df[['File', 'Throughput']]

#creo tabella "tabellaTh" con nome test e throughput
tabellaTh = pd.DataFrame(columns=['CTT', 'Throughput'])
tabellaTh['CTT'] = tabellaTh['CTT'].astype(int)

#scorro la matrice di tre in tre righe con un ciclo for

for i in range(0, len(df), 3):
    name=df.iloc[i]['File']
    name = name.replace("Dati/", "")
    split = str(name.split("C")[0])
    name = split


    df1=df.iloc[i:i+3]
    media=df1['Throughput'].mean()
    tabellaTh.loc[i]=[name, media]

#salvo la tabella in un file csv
tabellaTh.to_csv('tabellaTh.csv', index=False)

#creo un grafico con sull'asse x i CTT e sull'asse y il throughput utilizzando la tabella appena creata


tabellaTh.plot(x='CTT', y='Throughput', title='Throughput per CTT', marker='o', color='blue')
#salvo l'immagine del grafico creato
plt.savefig('throughput_per_ctt.png')


#SCRIPT RESPONSE TIME

# Importa i dati
df = pd.read_csv("statistiche.csv")

#voglio solo label e throughput
df = df[['File', 'ResponseTime']]

#creo tabella "tabellaTh" con CTT e RT
tabellaRT = pd.DataFrame(columns=['CTT', 'ResponseTime'])

#scorro la matrice di tre in tre righe con un ciclo for

for i in range(0, len(df), 3):
    name=df.iloc[i]['File']
    name = name.replace("Dati/", "")
    split = str(name.split("C")[0])
    name = split


    df1=df.iloc[i:i+3]
    media=df1['ResponseTime'].mean()
    tabellaRT.loc[i]=[name, media]

#salvo la tabella in un file csv
tabellaRT.to_csv('tabellaRT.csv', index=False)

#creo un grafico con sull'asse x i CTT e sull'asse y il response time utilizzando la tabella appena creata


tabellaRT.plot(x='CTT', y='ResponseTime', title='Response Time per CTT', marker='o', color='blue')

#salvo l'immagine del grafico creato
plt.savefig('response_time_per_ctt.png')

#SCRIPT POWER
#leggo tabellaRT.csv e tabellaTh.csv e calcolo il power per ogni CTT che è uguale a throughput/RT

# Importa i dati
df = pd.read_csv("tabellaTh.csv")
df2 = pd.read_csv("tabellaRT.csv")

#creo la tabella power per ctt
tabellaPower = pd.DataFrame(columns=['CTT', 'Power'])

#scorro la matrice df

for i in range(0, len(df)):
    name=df.iloc[i]['CTT']
    th=df.iloc[i]['Throughput']
    rt=df2.iloc[i]['ResponseTime']
    power=th/rt
    tabellaPower.loc[i]=[name, power]

#salvo la tabella in un file csv
tabellaPower.to_csv('tabellaPower.csv', index=False)

#creo un grafico con sull'asse x i CTT e sull'asse y il power utilizzando la tabella appena creata


tabellaPower.plot(x='CTT', y='Power', title='Power per CTT', marker='o', color='blue')
#salvo l'immagine del grafico creato
plt.savefig('power_per_ctt.png')


#da rivedere grafici distanza asse x non corretta

