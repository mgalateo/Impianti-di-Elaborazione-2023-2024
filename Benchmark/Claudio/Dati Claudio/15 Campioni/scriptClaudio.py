import pandas as pd

def calcola_media(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]

    values = [float(line.split()[1]) for line in lines]

    averages = [sum(values[i:i+5]) / 5 for i in range(0, len(values), 5)]

    return averages

# Percorsi dei tuoi file .txt
file_paths = ['1K.txt', '100K.txt', '1M.txt']

# Calcola le medie per ciascun file
medie_file1 = calcola_media(file_paths[0])
medie_file2 = calcola_media(file_paths[1])
medie_file3 = calcola_media(file_paths[2])

# Crea i DataFrame per ciascun file
df1 = pd.DataFrame({'Medie 1K': medie_file1})
df2 = pd.DataFrame({'Medie 100K': medie_file2})
df3 = pd.DataFrame({'Medie 1M': medie_file3})

# Combina i DataFrame in uno unico
df_totale = pd.concat([df1, df2, df3], axis=1)

# Stampa il DataFrame totale
print(df_totale)

excel_path = ('Medie.xlsx')
df_totale.to_excel(excel_path, index=False, sheet_name='medie')