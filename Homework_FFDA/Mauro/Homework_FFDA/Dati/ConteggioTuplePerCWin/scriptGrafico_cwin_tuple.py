from matplotlib import pyplot as plt
import numpy as np

#leggo il file di testo
file = open("Dati/ConteggioTuplePerCWin/tupleCount-BGLErrorLog.txt", "r")
#creo una lista con tutte le righe del file

#creo una lista con tutte le righe del file
lines = file.readlines()
#creo una lista vuota per salvare i valori di cwin
cwin = []
#creo una lista vuota per salvare i valori di tuple

tuple = []

#creo un ciclo for per scorrere tutte le righe del file
for line in lines:
    #divido la riga in due parti, separando le due colonne
    parts = line.split()
    #salvo la prima parte della riga nella lista cwin
    cwin.append(int(parts[0]))
    #salvo la seconda parte della riga nella lista tuple
    tuple.append(int(parts[1]))

#creo un grafico con i valori di cwin e tuple
plt.plot(cwin, tuple, '-o')
# imposto le posizioni delle tacche sull'asse x ogni 100 unità
plt.xticks(np.arange(0, 2000, 100))
# creo una griglia con linee principali e sottili
plt.grid(which='major', axis='both', linestyle=':', linewidth=0.5)
#imposto il titolo del grafico
plt.title("Conteggio tuple per cwin")
#imposto l'etichetta dell'asse x
plt.xlabel("cwin")
#imposto l'etichetta dell'asse y
plt.ylabel("tuple")
#mostro il grafico
plt.show()

#chiudo il file
file.close()
