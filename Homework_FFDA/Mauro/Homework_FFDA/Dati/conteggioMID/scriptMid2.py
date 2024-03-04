import pandas as pd
import numpy as np
import os as os
import matplotlib.pyplot as plt 
import glob as glob

cartella = "logPerRack/"

# Crea una lista di percorsi per tutti i file csv nella cartella /Dati
log_files = glob.glob(cartella+"*")
fileRisultati= open("risultati.txt", "w")
for log_file in log_files:
    #leggo il file di testo txt contentente i log del blue gene
    logfiled = open(log_file,"r")
    loglines = logfiled.readlines()
    count_m0 = 0
    count_m1 = 0
    for j in range(len(loglines)):
        #line è una lista che contiene varie stringhe ottenute splittando l'entry corrente rispetto al carattere " " (spazio)
        line = loglines[j].split()
        #se il nodo della log entry corrente è uguale a quello di interesse
        ri = line[1].split('-')[1]
        if ri == "M0":
            count_m0 = count_m0 + 1
        if ri == "M1":
            count_m1 = count_m1 + 1
    rack = log_file.replace(cartella, "")
    rack = rack.replace(".txt", "")

    logfiled.close()
    fileRisultati.write(rack + " " + str(count_m0) + " " + str(count_m1) + "\n")
fileRisultati.close()

#leggo il file testuale risultati.txt e lo salvo in un dataframe contenente tre colonne rack, m0, m1
df = pd.read_csv("risultati.txt", sep=" ", header=None)
df.columns = ["Rack", "M0", "M1"]
#ordino il dataframe in base al rack
df = df.sort_values(by=['Rack'])

#creo un grafico a barre con i valori di m0 e m1 per ogni rack
fig, ax = plt.subplots()
barWidth = 0.3
r1 = np.arange(len(df['Rack']))
r2 = [x + barWidth for x in r1]
ax.bar(r1, df['M0'], width=barWidth, label='M0')
ax.bar(r2, df['M1'], width=barWidth, label='M1')
ax.set_xticks([r + barWidth for r in range(len(df['Rack']))])
ax.set_xticklabels(df['Rack'])
ax.legend()
plt.xticks(rotation=90)
plt.gcf().set_size_inches(20, 10)
plt.savefig("MID.png", dpi=300, bbox_inches='tight')
plt.close()

