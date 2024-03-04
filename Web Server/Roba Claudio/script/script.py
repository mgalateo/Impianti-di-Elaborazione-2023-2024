import pandas as pd
import os
import matplotlib.pyplot as plt

cartella = "C:\\Users\\claud\\Desktop\\script"

elenco_file_csv = [file for file in os.listdir(cartella) if file.endswith('.csv')]


risultati = []

for file_csv in elenco_file_csv:
    
    percorso_csv = os.path.join(cartella, file_csv)
    
    df = pd.read_csv(percorso_csv, header=0)
    
   
    timeStamp = df['timeStamp'].to_numpy()
    max_ts = timeStamp.max()
    min_ts = timeStamp.min()
    duration = ((max_ts) - (min_ts)) / 1000
    richieste_ok = df.query("responseMessage == 'OK'").count()['responseMessage']
    throughtput = richieste_ok / duration
    ResponseTime = df['elapsed'].mean()
    Power = throughtput / ResponseTime
    

    risultati.append({
        "File": file_csv,
        "Duration": duration,
        "Numero Richieste Valide": richieste_ok,
        "Throughtput": throughtput,
        "ResponseTime": ResponseTime,
        "Power": Power
    })



risultati_th = pd.DataFrame(risultati)

def custom_sort(file_name):
    parts = file_name.split('_')
    return int(parts[0].replace('CTT', '')), int(parts[1].split('.')[0])

# Applica l'ordinamento personalizzato
risultati_th['Order'] = risultati_th['File'].apply(custom_sort)
risultati_th = risultati_th.sort_values(by='Order').drop('Order', axis=1)

print(risultati_th)

risultati_th.to_csv("Risultati/risultati.csv")

intervallo = 3
medie_th = []
medie_power = []
medie_response = []

def media_metriche(risultati_th, media, colonna):
    for i in range(0, len(risultati_th), intervallo):
        group = risultati_th.iloc[i:i+intervallo]
        media_gruppo = group[colonna].mean()
        media.append(media_gruppo)
    return media

print("Medie Througtput: ",media_metriche(risultati_th, medie_th, 'Throughtput'))
print("Medie Response Time:",media_metriche(risultati_th, medie_response, 'ResponseTime'))
print("Medie Power: ",media_metriche(risultati_th, medie_power, 'Power'))

risultati_th['Numeri'] = risultati_th['File'].str.extract(r'(\d+)')


ascisse = set(risultati_th['Numeri'].astype(int))
ascisse = list(ascisse)
ascisse_ordinati = sorted(ascisse)

def grafici(etichetta,media):
    x = ascisse_ordinati
    y = media
    plt.figure(figsize=(8, 6)) 
    plt.scatter(x, y, label=etichetta, color='blue', marker='o', linestyle='-')
    plt.plot(x,y,color='blue',linestyle='-')
    plt.xlabel('CTT')
    plt.ylabel(etichetta)
    #plt.show()
    plt.savefig(etichetta + '.png')

grafici('Throughtput',medie_th)
grafici('Response Time',medie_response)
grafici('Power',medie_power)