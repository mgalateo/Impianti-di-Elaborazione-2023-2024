#!/bin/bash

clear

# Riavvia il server Apache
sudo systemctl restart apache2

# Attendi 2 secondi
sleep 2

echo server riavviato

# Genera un nome univoco per il file
data=$(date +%Y%m%d-%H%M%S)

# Avvia vmstat e salva i dati in un file
vmstat -n 1 305 > vmstat-$data.csv

# Elimina la prima riga del file
awk 'NR > 1 {print}' vmstat-$data.csv > vmstats-$data.csv

rm vmstat-$data.csv

echo report creato
