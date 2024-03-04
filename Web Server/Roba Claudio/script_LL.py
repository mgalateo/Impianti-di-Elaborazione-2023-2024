import csv

# Importa il file txt
with open("LL.txt", "r") as f:
    lines = f.readlines()
 
# Prendi la prima riga come intestazione
headers = lines[0].split()
 
# Estrai le colonne
data = [line.split() for line in lines[1:]]
 
# Crea un file csv
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(headers)
    writer.writerows(data)

