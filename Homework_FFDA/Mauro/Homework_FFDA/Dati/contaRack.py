#conteggio dei rack dal file di log blue gene
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os

#leggo il file di testo txt contentente i log del blue gene

with open('BGLErrorLog.txt', 'r') as file:
    data = file.read()

#chiudo il file
file.close()

listaRack = []
#per ogni riga di data

for line in data.split('\n'):
    #casting a stringa della riga
    stringa = str(line)
    #estraggo solo la seconda parola della riga
    secondaParola = stringa.split(' ')[1]
    #estraggo il valore precedente al carattere "-"
    rack = secondaParola.split('-')[0]
    #creo una lista con i valori estratti
    listaRack.append(rack)

#conto occorrenze dei rack
conteggioRack = pd.Series(listaRack).value_counts()
#ordino in maniera decrescente il conteggio dei rack
conteggioRack = conteggioRack.sort_values(ascending=False)

#creo un dataframe con i valori del conteggio dei rack
df = pd.DataFrame(conteggioRack)
#aggiungo una colonna con i rack
df['Rack'] = df.index
#rinomino le colonne
df.columns = ['Occorrenze', 'Rack']
#salvo il dataframe in un file xlxs
df.to_excel('conteggioRack.xlsx', index=False)
colors = plt.cm.viridis(np.linspace(0, 1, len(df)))
plt.bar(df['Rack'], df['Occorrenze'],color=colors)

plt.xticks(rotation=90)
#aumento dimensione del grafico
plt.gcf().set_size_inches(20, 10)
plt.savefig("conteggioPerRack.png", dpi=300, bbox_inches='tight')
plt.close()






