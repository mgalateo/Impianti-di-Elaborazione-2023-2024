import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm
import pandas as pd

# Dati di esempio

#leggere csv eliminando header
data_mauro1 = pd.read_csv('1000_mauro.csv',)
data_mauro1 = data_mauro1.iloc[:,0]
print(data_mauro1)

data_mauro2 = pd.read_csv('100000_mauro.csv')
data_mauro2 = data_mauro2.iloc[:,0]

data_mauro3 = pd.read_csv('1000000_mauro.csv')
data_mauro3 = data_mauro3.iloc[:,0]

#leggi xlsx
data_claudio = pd.read_excel('Medie.xlsx')

#prima colonna dell' xlsx
data_claudio1 = data_claudio.iloc[:,0]
data_claudio2 = data_claudio.iloc[:,1]
data_claudio3 = data_claudio.iloc[:,2]

print(data_claudio1)

# Calcolo degli intervalli di confidenza
ci1 = norm.interval(0.95, loc=np.mean(data_mauro1), scale=np.std(data_mauro1) / np.sqrt(len(data_mauro1)))
ci2 = norm.interval(0.95, loc=np.mean(data_claudio1), scale=np.std(data_claudio1) / np.sqrt(len(data_claudio1)))

media1= np.mean(data_mauro1)
media2= np.mean(data_claudio1)
std_dev1= np.std(data_mauro1)
std_dev2= np.std(data_claudio1)

print(media1)
print(std_dev1)
# Creazione di un array di valori x da -3*std_dev a 3*std_dev + media
x1 = np.linspace(media1 - 3*std_dev1, media1 + 3*std_dev1, 100)
x2 = np.linspace(media2 - 3*std_dev2, media2 + 3*std_dev2, 100)


# Calcoliamo la funzione di densità di probabilità (pdf) della distribuzione normale
y1 = norm.pdf(x1, media1, std_dev1)
y2 = norm.pdf(x2, media2, std_dev2)

fig,axs= plt.subplots(2,1,sharex=True,figsize=(10,10))
axs[0].plot(x1, y1, color='blue', label='Mauro')
axs[0].fill_between(x1, y1, color='blue', alpha=0.3)

axs[0].plot(x2, y2, color='orange', label='Claudio')
axs[0].fill_between(x2, y2, color='orange', alpha=0.3)
axs[0].axvline(ci1[0], linestyle='--', color='blue',  alpha=0.4)
axs[0].axvline(ci1[1], linestyle='--', color='blue',  alpha=0.4)
axs[0].axvline(ci2[0], linestyle='--', color='orange',  alpha=0.4)
axs[0].axvline(ci2[1], linestyle='--', color='orange',  alpha=0.4)
axs[0].legend()
axs[0].set_title('1K Corpi')
#aggiungo griglia e scala asse x
axs[0].grid(True)

axs[1].axvspan(ci1[0],ci1[1], linestyle='--', color='b',hatch="/",  alpha=0.4, label='CI Mauro', linewidth=2)
axs[1].axvspan(ci2[0],ci2[1], linestyle='--', color='orange',hatch="/",  alpha=0.4, linewidth=2)
axs[1].grid(True)
#salva il grafico
plt.savefig('1K_corpi2.png', dpi=600)

plt.close()

#creo lo stesso grafico ma con i 100K corpi
ci1 = norm.interval(0.95, loc=np.mean(data_mauro2), scale=np.std(data_mauro2) / np.sqrt(len(data_mauro2)))
ci2 = norm.interval(0.95, loc=np.mean(data_claudio2), scale=np.std(data_claudio2) / np.sqrt(len(data_claudio2)))

media1= np.mean(data_mauro2)
media2= np.mean(data_claudio2)
std_dev1= np.std(data_mauro2)
std_dev2= np.std(data_claudio2)


x1 = np.linspace(media1 - 3*std_dev1, media1 + 3*std_dev1, 100)
x2 = np.linspace(media2 - 3*std_dev2, media2 + 3*std_dev2, 100)


# Calcoliamo la funzione di densità di probabilità (pdf) della distribuzione normale
y1 = norm.pdf(x1, media1, std_dev1)
y2 = norm.pdf(x2, media2, std_dev2)

fig,axs= plt.subplots(2,1,sharex=True,figsize=(10,10))
axs[0].plot(x1, y1, color='blue', label='Mauro')
axs[0].fill_between(x1, y1, color='blue', alpha=0.3)

axs[0].plot(x2, y2, color='orange', label='Claudio')
axs[0].fill_between(x2, y2, color='orange', alpha=0.3)
axs[0].axvline(ci1[0], linestyle='--', color='blue',  alpha=0.4)
axs[0].axvline(ci1[1], linestyle='--', color='blue',  alpha=0.4)
axs[0].axvline(ci2[0], linestyle='--', color='orange',  alpha=0.4)
axs[0].axvline(ci2[1], linestyle='--', color='orange',  alpha=0.4)
axs[0].legend()
axs[0].set_title('100K Corpi')
#aggiungo griglia e scala asse x
axs[0].grid(True)

axs[1].axvspan(ci1[0],ci1[1], linestyle='--', color='b',hatch="/",  alpha=0.4, label='CI Mauro', linewidth=2)
axs[1].axvspan(ci2[0],ci2[1], linestyle='--', color='orange',hatch="/",  alpha=0.4, linewidth=2)
axs[1].grid(True)
#salva il grafico
plt.savefig('100K_corpi2.png', dpi=600)

plt.close()

#creo lo stesso grafico ma con i 1M corpi
ci1 = norm.interval(0.95, loc=np.mean(data_mauro3), scale=np.std(data_mauro3) / np.sqrt(len(data_mauro3)))
ci2 = norm.interval(0.95, loc=np.mean(data_claudio3), scale=np.std(data_claudio3) / np.sqrt(len(data_claudio3)))

media1= np.mean(data_mauro3)
media2= np.mean(data_claudio3)
std_dev1= np.std(data_mauro3)
std_dev2= np.std(data_claudio3)


x1 = np.linspace(media1 - 3*std_dev1, media1 + 3*std_dev1, 100)
x2 = np.linspace(media2 - 3*std_dev2, media2 + 3*std_dev2, 100)


# Calcoliamo la funzione di densità di probabilità (pdf) della distribuzione normale
y1 = norm.pdf(x1, media1, std_dev1)
y2 = norm.pdf(x2, media2, std_dev2)

fig,axs= plt.subplots(2,1,sharex=True,figsize=(10,10))
axs[0].plot(x1, y1, color='blue', label='Mauro')
axs[0].fill_between(x1, y1, color='blue', alpha=0.3)

axs[0].plot(x2, y2, color='orange', label='Claudio')
axs[0].fill_between(x2, y2, color='orange', alpha=0.3)
axs[0].axvline(ci1[0], linestyle='--', color='blue',  alpha=0.4)
axs[0].axvline(ci1[1], linestyle='--', color='blue',  alpha=0.4)
axs[0].axvline(ci2[0], linestyle='--', color='orange',  alpha=0.4)
axs[0].axvline(ci2[1], linestyle='--', color='orange',  alpha=0.4)
axs[0].legend()
axs[0].set_title('1M Corpi')
#aggiungo griglia e scala asse x
axs[0].grid(True)

axs[1].axvspan(ci1[0],ci1[1], linestyle='--', color='b',hatch="/",  alpha=0.4, label='CI Mauro', linewidth=2)
axs[1].axvspan(ci2[0],ci2[1], linestyle='--', color='orange',hatch="/",  alpha=0.4, linewidth=2)
axs[1].grid(True)
#salva il grafico
plt.savefig('1M_corpi2.png', dpi=600)

plt.close()

