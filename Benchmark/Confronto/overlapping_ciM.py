import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm
import pandas as pd

# Dati di esempio

#leggere csv
data_mauro1 = pd.read_csv('1000_mauro.csv')
data_mauro2 = pd.read_csv('100000_mauro.csv')
data_mauro3 = pd.read_csv('1000000_mauro.csv')

#leggi xlsx
data_claudio = pd.read_excel('Medie.xlsx')

#prima colonna dell' xlsx
data_claudio1 = data_claudio.iloc[:,0]
data_claudio2 = data_claudio.iloc[:,1]
data_claudio3 = data_claudio.iloc[:,2]

x1 = np.linspace(np.mean(data_mauro1) - 3*np.std(data_mauro1), np.mean(data_mauro1) + 3*np.std(data_mauro1), 100)
x2 = np.linspace(np.mean(data_claudio1) - 3*np.std(data_claudio1), np.mean(data_claudio1) + 3*np.std(data_claudio1), 100)

# Calcolo degli intervalli di confidenza
ci1 = norm.interval(0.95, loc=np.mean(data_mauro1), scale=np.std(data_mauro1) / np.sqrt(len(data_mauro1)))
ci2 = norm.interval(0.95, loc=np.mean(data_claudio1), scale=np.std(data_claudio1) / np.sqrt(len(data_claudio1)))

# Creazione del grafico
sns.kdeplot(data_mauro1, fill=True, label='1.000 Corpi - Mauro', color='blue', alpha=0.4)
sns.kdeplot(data_claudio1, fill=True, label='1.000 Corpi - Claudio', color='orange', alpha=0.4)

# Rappresentazione degli intervalli di confidenza
plt.axvline(ci1[0], linestyle='--', color='blue',  alpha=0.4)
plt.axvline(ci1[1], linestyle='--', color='blue',  alpha=0.4)
plt.axvline(ci2[0], linestyle='--', color='orange',  alpha=0.4)
plt.axvline(ci2[1], linestyle='--', color='orange',  alpha=0.4)

# Distribuzione Gaussiana per Mauro
gaussian_mauro = norm.pdf(x1, np.mean(data_mauro1), np.std(data_mauro1))
plt.plot(x1, gaussian_mauro, color='blue', linestyle='--', label='1.000 Corpi - Mauro (Gaussiana)')

# Distribuzione Gaussiana per Claudio
gaussian_claudio = norm.pdf(x2, np.mean(data_claudio1), np.std(data_claudio1))
plt.plot(x2, gaussian_claudio, color='orange', linestyle='--', label='1.000 Corpi - Claudio (Gaussiana)')


# Etichette e legenda
plt.xlabel('Valore')
plt.ylabel('Densità di probabilità')
plt.legend()

#salva il grafico
plt.savefig('1K_corpi2.png')

#chiudere plot
plt.close()


# Calcolo degli intervalli di confidenza
ci1 = norm.interval(0.95, loc=np.mean(data_mauro2), scale=np.std(data_mauro2) / np.sqrt(len(data_mauro2)))
ci2 = norm.interval(0.95, loc=np.mean(data_claudio2), scale=np.std(data_claudio2) / np.sqrt(len(data_claudio2)))

# Creazione del grafico
sns.kdeplot(data_mauro2, fill=True, label='100K Corpi - Mauro', color='blue', alpha=0.4)
sns.kdeplot(data_claudio2, fill=True, label='100K Corpi - Claudio', color='orange', alpha=0.4)

# Rappresentazione degli intervalli di confidenza
plt.axvline(ci1[0], linestyle='--', color='blue',  alpha=0.4)
plt.axvline(ci1[1], linestyle='--', color='blue',  alpha=0.4)
plt.axvline(ci2[0], linestyle='--', color='orange',  alpha=0.4)
plt.axvline(ci2[1], linestyle='--', color='orange',  alpha=0.4)

# Etichette e legenda
plt.xlabel('Valore')
plt.ylabel('Densità di probabilità')
plt.legend()



#salva il grafico
plt.savefig('100K_corpi2.png')

#chiudere plot
plt.close()



# Calcolo degli intervalli di confidenza
ci1 = norm.interval(0.95, loc=np.mean(data_mauro3), scale=np.std(data_mauro3) / np.sqrt(len(data_mauro3)))
ci2 = norm.interval(0.95, loc=np.mean(data_claudio3), scale=np.std(data_claudio3) / np.sqrt(len(data_claudio3)))

# Creazione del grafico
sns.kdeplot(data_mauro3, fill=True, label='1M Corpi - Mauro', color='blue', alpha=0.4)
sns.kdeplot(data_claudio3, fill=True, label='1M Corpi - Claudio', color='orange', alpha=0.4)

# Rappresentazione degli intervalli di confidenza
plt.axvline(ci1[0], linestyle='--', color='blue',  alpha=0.4)
plt.axvline(ci1[1], linestyle='--', color='blue',  alpha=0.4)
plt.axvline(ci2[0], linestyle='--', color='orange',  alpha=0.4)
plt.axvline(ci2[1], linestyle='--', color='orange',  alpha=0.4)

# Etichette e legenda
plt.xlabel('Valore')
plt.ylabel('Densità di probabilità')
plt.legend()


#salva il grafico
plt.savefig('1M_corpi2.png')

#chiudere plot
plt.close()


