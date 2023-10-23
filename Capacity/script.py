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
    "CTT",
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
    ctt=csv_file.replace("Dati/", "")
    ctt = ctt.split("C")[0]
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
        ctt,
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
#rendo CTT un intero
results['CTT'] = results['CTT'].astype(int)
results = results.sort_values(by=["CTT","File"])


# Salva il DataFrame in un file CSV
results.to_csv("statistiche.csv", index=False)
results = results.sort_values(by=["CTT"])

df=results

#voglio solo label e throughput
df = df[['CTT', 'Throughput']]

#creo tabella "tabellaTh" con nome test e throughput
tabellaTh = pd.DataFrame(columns=['CTT', 'Throughput'])
tabellaTh['CTT'] = tabellaTh['CTT'].astype(int)

#scorro la matrice di tre in tre righe con un ciclo for

for i in range(0, len(df), 3):
    name=df.iloc[i]['CTT']


    df1=df.iloc[i:i+3]
    media=df1['Throughput'].mean()
    tabellaTh.loc[i]=[name, media]

#salvo la tabella in un file csv
tabellaTh.to_csv('tabellaTh.csv', index=False)


df=results

#voglio solo label e throughput
df = df[['CTT', 'ResponseTime']]

#creo tabella "tabellaTh" con CTT e RT
tabellaRT = pd.DataFrame(columns=['CTT', 'ResponseTime'])

#scorro la matrice di tre in tre righe con un ciclo for

for i in range(0, len(df), 3):
    name=df.iloc[i]['CTT']


    df1=df.iloc[i:i+3]
    media=df1['ResponseTime'].mean()
    tabellaRT.loc[i]=[name, media]

#salvo la tabella in un file csv
tabellaRT.to_csv('tabellaRT.csv', index=False)

#creo la tabella power per ctt
tabellafinale = pd.DataFrame(columns=['CTT','Throughput','Response Time','Power'])
tabellafinale['CTT']=tabellaTh['CTT']
tabellafinale['Throughput']=tabellaTh['Throughput']
tabellafinale['Response Time']=tabellaRT['ResponseTime']
tabellafinale['Power']=tabellaTh['Throughput']/tabellaRT['ResponseTime']

tabellafinale.to_csv('tabellafinale.csv', index=False)

df=tabellafinale


tabellafinale1 = pd.DataFrame(columns=['CTT','Throughput','Response Time','Power'])
tabellafinale2 = pd.DataFrame(columns=['CTT','Throughput','Response Time','Power'])

for i in range(0, len(df)):

    if df.iloc[i]['CTT']<=6500:
        tabellafinale1.loc[i]=[df.iloc[i]['CTT'],df.iloc[i]['Throughput'],df.iloc[i]['Response Time'],df.iloc[i]['Power']]
    if df.iloc[i]['CTT']>=6500:
        tabellafinale2.loc[i]=[df.iloc[i]['CTT'],df.iloc[i]['Throughput'],df.iloc[i]['Response Time'],df.iloc[i]['Power']]


# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(tabellafinale2['CTT'], tabellafinale2['Power'], 'o--', linewidth=1,color='black')
plt.plot(tabellafinale1['CTT'], tabellafinale1['Power'], 'o-', linewidth=2,color='green')
#plt.plot(df["CTT"], df["Power"], marker="o", color="green")
plt.xlabel("CTT")
plt.ylabel("Power")
plt.title("Power per CTT")
plt.grid(True)
plt.savefig("power_per_ctt_con_sfumatura.png")

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(tabellafinale2['CTT'], tabellafinale2['Throughput'], 'o--', linewidth=1,color='black')
plt.plot(tabellafinale1['CTT'], tabellafinale1['Throughput'], 'o-', linewidth=2,color='blue')
#plt.plot(df["CTT"], df["Power"], marker="o", color="green")
plt.xlabel("CTT")
plt.ylabel("Throughput")
plt.title("Throughput per CTT")
plt.grid(True)
plt.savefig("throughput_per_ctt_con_sfumatura.png")


# Crea il grafico
plt.figure(figsize=(10, 6))
plt.plot(tabellafinale2['CTT'], tabellafinale2['Response Time'], 'o--', linewidth=1,color='black')
plt.plot(tabellafinale1['CTT'], tabellafinale1['Response Time'], 'o-', linewidth=2,color='Red')
#plt.plot(df["CTT"], df["Power"], marker="o", color="green")
plt.xlabel("CTT")
plt.ylabel("Response Time")
plt.title("Response Time per CTT")
plt.grid(True)
plt.savefig("response_time_per_ctt_con_sfumatura.png")