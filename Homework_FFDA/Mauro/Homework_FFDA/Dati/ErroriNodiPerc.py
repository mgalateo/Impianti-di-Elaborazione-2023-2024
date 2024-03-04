import pandas as pd
import numpy as np
import os

#leggo i dati da corrErroriNodiCategorie.csv con header e tutte le colonne tranne la prima sono di tipo float
df = pd.read_csv('corrErroriNodiCategorie.csv', header=0)

#la colonna DEV MEM IO NET PRO OTH sono float
#la colonna NODO è stringa
#aggiusto i tipi
df['DEV'] = df['DEV'].astype(float)
df['MEM'] = df['MEM'].astype(float)
df['IO'] = df['IO'].astype(float)
df['NET'] = df['NET'].astype(float)
df['PRO'] = df['PRO'].astype(float)
df['OTH'] = df['OTH'].astype(float)


#creo una nuova colonna con la somma delle colonne DEV MEM IO NET PRO OTH
df['TOT'] = df['DEV'] + df['MEM'] + df['IO'] + df['NET'] + df['PRO'] + df['OTH']

#sostiuisco i valori delle colonne con il valore precedente diviso il totalenella colonna TOT
df['DEV'] = df['DEV']/df['TOT']*100
df['MEM'] = df['MEM']/df['TOT']*100
df['IO'] = df['IO']/df['TOT']*100
df['NET'] = df['NET']/df['TOT']* 100
df['PRO'] = df['PRO']/df['TOT']*100
df['OTH'] = df['OTH']/df['TOT']*100

print (df)
#elimino la colonna TOT
df.drop('TOT', axis=1, inplace=True)

#salvo il dataframe in un file xlsx
df.to_excel('corrErroriNodiCategoriePercentuali.xlsx', index=False)
#df4 = le ultime 3 righe di df
df4 = df.tail(3)

#estraggo i le prime 7 righe del dataframe e le salvo in un nuovo dataframe df2 senza la prima colonna

df2 = df.head(7)
df2.drop('Nodo', axis=1, inplace=True)
print (df2)
#calcolo la media delle colonne DEV MEM IO NET PRO OTH e la salvo in un nuovo dataframe df3 con una sola riga con nome nodo "Computazionali"
df3 = pd.DataFrame(df2.mean()).T
#aggiungi la colonna NODO con valore "Computazionali" come prima colonna
df3.insert(0, 'Nodo', 'Computazionali')
#aggiungi a df3 le restanti righe di df

df3 = pd.concat([df3, df4])
print (df3)
#salvo il dataframe in un file xlsx
df3.to_excel('corrErroriNodiCategoriePercentualiMedia.xlsx', index=False)



