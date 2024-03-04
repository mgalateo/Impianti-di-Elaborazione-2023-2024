#leggo il file excel conteggioRack.xlxs
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import shutil
import re

#leggo il path del file di log e il campo su cui effettuare il filtraggio
logfile = 'BGLErrorLog.txt'
logfiled = open(logfile,"r")
loglines = logfiled.readlines()



df = pd.read_excel('conteggioRack.xlsx')
#estraggo solo la colonna rack senza l'indice in un vettore
rack = df['Rack'].values

for i in range(len(rack)):
    #apri un file in scrittura per collezionare i risultati
    nameFile=rack[i]+".txt"
    f = open(nameFile, 'w')
    #scandisco tutte le entry del log
    for j in range(len(loglines)):
        #line è una lista che contiene varie stringhe ottenute splittando l'entry corrente rispetto al carattere " " (spazio)
        line = loglines[j].split()
        #se il nodo della log entry corrente è uguale a quello di interesse
        ri = line[1].split('-')[0]
        if ri == rack[i]:
            #scrivi la log entry corrente nel file di output
            f.write(loglines[j])
    #chiudo il file
    f.close()
#chiudo il file
    
logfiled.close()

