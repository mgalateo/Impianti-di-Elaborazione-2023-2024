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

df4=pd.DataFrame()

matrice=pd.DataFrame()

# Itera sulla lista di percorsi e calcola il throughput e il tempo di risposta medio per ciascun file
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    ctt=csv_file.replace("Dati/", "")
    ctt = ctt.split("C")[0]
    df['responseCode'] = df['responseCode'].astype(str)
    

    dfRigheOk = df[df['responseCode'] == "200"]
    
    # Rimuovi "Group 1-" dalla colonna 'threadName' utilizzando .loc
    dfRigheOk.loc[:, 'threadName'] = dfRigheOk['threadName'].str.replace('Thread Group 1-', '')
    # Raggruppa per 'threadName' e conta le occorrenze
    occurrences = dfRigheOk['threadName'].value_counts()

    df1=pd.DataFrame()
    df1['threadName']=occurrences.index
    df1['nRichieste']=occurrences.values
    #trasformo la colonna threadName in intero
    df1['threadName'] = df1['threadName'].astype(int)

    #ordino df1 per threadName
    df1=df1.sort_values(by='threadName')

    df1.set_index('threadName', inplace=True)
    
    #creo una matrice che contiene una colonna nome file e una colonna CTT , e 100 colonne della trasposta di df1
    #trasformo la trasposta di df1 in una matrice
    matrice=df1.transpose()

    #aggiungo le colonne nome file e CTT alla matrice
    matrice.insert(0, 'File', csv_file.split("/")[-1])
    matrice.insert(1, 'CTT', ctt)

    #aggiungo la matrice alla matrice dei risultati
    df4 = pd.concat([df4, matrice], axis=0, ignore_index=True)

#rendo CTT un intero
df4['CTT'] = df4['CTT'].astype(int)
df4 = df4.sort_values(by=["CTT","File"])
#salva la matrice dei risultati su disco
df4.to_csv("RichiestePerThread.csv", index=False)
    

#fairness generica
#leggo il file csv tabellafinale.csv e mi estrggo i valori di throughput fino a ctt=6000
df5=pd.read_csv("tabellafinale.csv")
df5=df5[['CTT','Throughput']]

#calcolo del throughput normalizzato
#per ogni riga calcolo il throughput normalizzato come throughput * 60 / ctt
df5['ThroughputNorm'] = df5.apply(lambda row: row['Throughput']*60/row['CTT'], axis=1)


#print(df5)

#calcolo della fairness calcolata come la somma della colonna throughput normalizzato al quadrato diviso il numero di righe per somma dei quadrati della colonna throughput normalizzato
fairness=df5['ThroughputNorm'].sum()**2/df5['ThroughputNorm'].pow(2).sum()/len(df5.index)
#print("Fairness: ", fairness)

#esporto in un txt il valore di fairness calcolato e la matrice df5
file = open("fairness.txt", "w")
file.write("Fairness: "+str(fairness)+"\n")
file.write(str(df5))
file.close()

###fine calcolo fairness generica

#dichiaro results come una matrice di dimensioni 102 colonne come righe il numero di file ovvero la lunghezza di csv_files. NON COME DATAFRAME
matrice = np.empty((len(csv_files), 102), dtype=object)
matriceD = np.empty((len(csv_files), 102), dtype=object)
matriceN = np.empty((len(csv_files), 102), dtype=object)
matriceFairness = np.empty((len(csv_files), 3), dtype=object)
j=0
#calcolo duration per ogni thread per ogni file
for csv_file in csv_files:
    d = pd.read_csv(csv_file)
    ctt=csv_file.replace("Dati/", "")
    ctt = ctt.split("C")[0]
    #trasformo ctt in un intero
    ctt = int(ctt)
    d['responseCode'] = d['responseCode'].astype(str)
    
    matrice[j][0]=csv_file.split("/")[-1]
    matrice[j][1]=ctt
    
    matriceN[j][0]=csv_file.split("/")[-1]
    matriceN[j][1]=ctt

    matriceD[j][0]=csv_file.split("/")[-1]
    matriceD[j][1]=ctt

    matriceFairness[j][0]=csv_file.split("/")[-1]
    matriceFairness[j][1]=ctt



    dfRigheOk = d[d['responseCode'] == "200"]
    # Rimuovi "Group 1-" dalla colonna 'threadName' utilizzando .loc
    dfRigheOk.loc[:, 'threadName'] = dfRigheOk['threadName'].str.replace('Thread Group 1-', '')
    #rendo intero la colonna threadName

    dfRigheOk['threadName'] = dfRigheOk['threadName'].astype(int)

    #creo un ciclo for dove ad ogni ciclo salvo la matrice con threadName senza "Group 1-" in maniera incrementale , quindi threadName=1, threadName=2, threadName=3 ecc
    for i in range(1,101):       

        #copio in un dataframe solo le righe con threadName=i
        dfRigheOk2 = dfRigheOk[dfRigheOk['threadName'] == i]
        durataMax=max(dfRigheOk2['timeStamp'])
        durataMin=min(dfRigheOk2['timeStamp'])

        duration=(durataMax-durataMin)/1000
        matriceD[j][i+1]=duration

        throughput=len(dfRigheOk2)/duration

        matrice[j][i+1]=throughput

        matriceN[j][i+1]=(throughput * 60)/(ctt / 100)
    
    #somma è data dalla somma della riga corrente j della matriceN esclusi i primi due elementi
    somma=matriceN[j][2:].sum()
    qsomma=somma**2

    #devo calcolare il quadrato di ogni elemento della riga corrente j della matriceN esclusi i primi due elementi e sommarli tra loro
    sommaQ=0
    for i in range(2,102):
        sommaQ=sommaQ+matriceN[j][i]**2


    fairness=qsomma/sommaQ/100
    matriceFairness[j][2]=fairness


        
    j=j+1



#esporto la matrice in un file csv
np.savetxt("ThXThread.csv", matrice, delimiter=",", fmt='%s')

np.savetxt("DurationXThread.csv", matriceD, delimiter=",", fmt='%s')

np.savetxt("NormalizedThXThread.csv", matriceN, delimiter=",", fmt='%s')

np.savetxt("FairnessXThread.csv", matriceFairness, delimiter=",", fmt='%s')

#calcolo la media della matriceFainess ogni tre righe mantenendo il valore di ctt
matriceFairnessMedia = np.empty((len(csv_files)//3, 2), dtype=object)
for i in range(0, len(matriceFairness), 3):
    matriceFairnessMedia[i//3][0]=matriceFairness[i][1]
    matriceFairnessMedia[i//3][1]=(matriceFairness[i][2]+matriceFairness[i+1][2]+matriceFairness[i+2][2])/3

#trtaformo la matrice in un dataframe ed ordino in base alla prima colonna ctt in ordine crescente, la prima colonna sarà ctt e la seconda sarà la media della fairness
dfFairnessMedia=pd.DataFrame(matriceFairnessMedia)
dfFairnessMedia=dfFairnessMedia.sort_values(by=0)
dfFairnessMedia.columns=['CTT','Fairness']
dfFairnessMedia['CTT'] = dfFairnessMedia['CTT'].astype(int)



dfFairnessMedia.to_csv("FairnessXThreadMedia.csv", index=False)


dfFairnessRisorse=pd.DataFrame(columns=['File','CTT','Fairness'])
#calcolo la fairness per ogni file tra le varie risorse (nome contenuto nella colonna label)

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    ctt=csv_file.replace("Dati/", "")
    ctt = ctt.split("C")[0]
    df['responseCode'] = df['responseCode'].astype(str)
    

    dfRigheOk = df[df['responseCode'] == "200"]
    richiesteTot=len(dfRigheOk)

    # Raggruppa per 'label' (nome della richiesta) e conta le occorrenze
    occurrences = dfRigheOk['label'].value_counts()

    durataMax=max(dfRigheOk['timeStamp'])
    durataMin=min(dfRigheOk['timeStamp'])

    duration=(durataMax-durataMin)/1000

    dfR=pd.DataFrame()
    dfR['NomeRichiesta']=occurrences.index
    dfR['nRichieste']=occurrences.values

    #aggiungo la colonna throughput a dfR e la calcolo come nRichieste/duration per ogni riga di dfR
    dfR['Throughput']=dfR.apply(lambda row: row['nRichieste']/duration, axis=1)

    #aggiungo la colonna throughput normalizzato calcolato come throughput * 60 / (ctt/6) per ogni riga di dfR
    dfR['ThroughputNorm']=dfR.apply(lambda row: row['Throughput']*60/(int(ctt)/6), axis=1)
    #ordino dfR per threadName
    dfR=dfR.sort_values(by='NomeRichiesta')

    somma2=dfR['ThroughputNorm'].sum()
    qsomma2=somma2**2

    sommaQ2=0
    for i in range(0,len(dfR.index)):
        sommaQ2=sommaQ2+dfR['ThroughputNorm'].iloc[i]**2
    
    fairness2=qsomma2/sommaQ2/6

    #aggiungo per ogni file la riga con nome file, ctt e fairness2 alla matrice dfFairnessRisorse
    dfFairnessRisorse.loc[len(dfFairnessRisorse)] = [
        csv_file.split("/")[-1],
        ctt,
        fairness2,
    ]

    #salvo dfR su disco con il nome file csv_file.split("/")[-1] .csv nella cartella Fairness/fairnessRisorsePerFile
    dfR.to_csv("Fairness/fairnessRisorsePerFile/"+csv_file.split("/")[-1]+".csv", index=False)

#ordina(dfFairnessRisorse) in base alla prima colonna ctt in ordine crescente e nome file in ordine alfabetico e salva su disco
dfFairnessRisorse=dfFairnessRisorse.sort_values(by=['CTT','File'])
dfFairnessRisorse.to_csv("FairnessRisorse.csv", index=False)







