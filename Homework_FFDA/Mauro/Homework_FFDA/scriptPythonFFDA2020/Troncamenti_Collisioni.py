import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

istanzeMerc=pd.DataFrame()

width = [10,9,3,100]


for i in range(1,509):
    
    doc=pd.read_fwf('tupling_MercuryErrorLog-200/tuple'+str(i)+'.txt', widths=width, names = ['Timestamp','Node','Subsystem','Message'])
    doc.insert(4, 'Tupla', str(i), True)
    istanzeMerc = pd.concat([istanzeMerc, doc])

istanzeMerc['Tupla']=pd.to_numeric(istanzeMerc['Tupla'])


trunc_countMerc = 0 
nodiMerc_list = []
nodiMerc = pd.DataFrame()

for t in istanzeMerc['Tupla'].unique():
    if t != 508:
        mask = (istanzeMerc['Tupla']==t)
        mask_next = (istanzeMerc['Tupla']==t+1)
        istanze_filtrate = istanzeMerc.loc[mask]
        istanze_filtrate_next = istanzeMerc.loc[mask_next]
        if (istanze_filtrate.loc[istanze_filtrate.shape[0]-1, :].Node== istanze_filtrate_next.loc[0, :].Node):
            trunc_countMerc = trunc_countMerc + 1
            
            #aggiungo al dataframe nodiMerc la tupla che ha causato il troncamento
            nodiMerc_list.append(istanze_filtrate.loc[istanze_filtrate.shape[0]-1, :])
    else:
        print("il file è finito")

print('Troncamenti : ' + str(trunc_countMerc))
print('Percentuale di troncamenti: '+str(trunc_countMerc/508*100)+' %')

#trasformo la lista in dataframe e raggruppo per nodo
nodiMerc = pd.DataFrame(nodiMerc_list)

#ordino i nodi per numero di troncamenti in ordine decrescente
nodiMerc = nodiMerc.groupby(by='Node').count().Timestamp.sort_values(ascending=False)

colors = plt.cm.viridis(np.linspace(0, 1, len(nodiMerc)))
plt.bar(nodiMerc.index, nodiMerc.values,color=colors)

plt.xlabel("Nodi")
plt.ylabel("Num Troncamenti")
plt.title("Troncamenti per nodo")
#aggiungo una nota con il totale dei troncamenti
plt.annotate('Totale troncamenti: '+str(trunc_countMerc), xy=(0.05, 0.95), xycoords='axes fraction')
#aumento dimensione del grafico
plt.gcf().set_size_inches(20, 10)
plt.savefig("Troncamenti per nodo Mercury.png", dpi=300, bbox_inches='tight')
plt.close()

#BGL
istanzeBGL=pd.DataFrame()
width = [10,10,8,100]

for i in range(1,404):
    doc=pd.read_fwf('tupling_BGLErrorLog-200/tuple'+str(i)+'.txt', widths=width, names = ['Timestamp','Node','Card','Message'])
    doc.loc[doc['Card'].str.contains('J18'),'Card type'] = 'I-O'
    doc.loc[~doc['Card'].str.contains('J18'),'Card type'] = 'computation'
    doc.insert(4, 'Tupla', str(i), True)
    istanzeBGL = pd.concat([istanzeBGL, doc])
    
istanzeBGL['Tupla']=pd.to_numeric(istanzeBGL['Tupla'])
istanzeBGL

trunc_countBGL = 0
nodiBGL = pd.DataFrame()
nodiBGL_list = []

for t in istanzeBGL['Tupla'].unique():
    if t != 403:
        mask = (istanzeBGL['Tupla']==t)
        mask_next = (istanzeBGL['Tupla']==t+1)
        istanze_filtrate_bgl = istanzeBGL.loc[mask]
        istanze_filtrate_next_bgl = istanzeBGL.loc[mask_next]
        if (istanze_filtrate_bgl.loc[istanze_filtrate_bgl.shape[0]-1, :].Node== istanze_filtrate_next_bgl.loc[0, :].Node):
            trunc_countBGL = trunc_countBGL + 1
        
            #aggiungo al dataframe nodiBGL la tupla che ha causato il troncamento
            nodiBGL_list.append(istanze_filtrate_bgl.loc[istanze_filtrate_bgl.shape[0]-1, :])
            
    else:
        print("il file è finito")

print('Troncamenti : ' + str(trunc_countBGL))
print('Percentuale di troncamenti: '+str(trunc_countBGL/403*100)+' %')

#trasformo la lista in dataframe e raggruppo per nodo
nodiBGL = pd.DataFrame(nodiBGL_list)

#ordino i nodi per numero di troncamenti in ordine decrescente
nodiBGL = nodiBGL.groupby(by='Node').count().Timestamp.sort_values(ascending=False)
plt.bar(nodiBGL.index, nodiBGL.values,color=colors)

plt.xlabel("Nodi")
plt.ylabel("Num Troncamenti")
plt.title("Troncamenti per nodo")
#aggiungo una nota con il totale dei troncamenti
plt.annotate('Totale troncamenti: '+str(trunc_countBGL), xy=(0.05, 0.95), xycoords='axes fraction')
#aumento dimensione del grafico
plt.gcf().set_size_inches(20, 10)
plt.savefig("Troncamenti per nodo BGL.png", dpi=300, bbox_inches='tight')
plt.close()

# # Script per le collisioni
coll_countMerc = 0
collMerc = {}

for t in istanzeMerc['Tupla'].unique():
    if t != 508:
        mask = (istanzeMerc['Tupla']==t)
        istanze_filtrate = istanzeMerc.loc[mask]
        if (len(istanze_filtrate.Node.unique())>1):
            coll_countMerc = coll_countMerc+1
            collMerc[t]=istanze_filtrate.Node.unique()
    else:
        print('File finito')
print('Collisioni Mercury : ' + str(coll_countMerc))



coll_countBGL_cardtype = 0
collBGL_cardtype = {}

for t in istanzeBGL['Tupla'].unique():
    if t != 403:
        mask = (istanzeBGL['Tupla']==t)
        istanze_filtrate = istanzeBGL.loc[mask]
        if (len(istanze_filtrate['Card type'].unique())>1):
            coll_countBGL_cardtype = coll_countBGL_cardtype+1
        
            collBGL_cardtype[t]=istanze_filtrate['Card type'].unique()
    else:
        print('File finito')
print('Collisioni BGL: ' + str(coll_countBGL_cardtype))


coll_countBGL_cardtype = 0
collBGL_cardtype = {}

for t in istanzeBGL['Tupla'].unique():
    if t != 403:
        mask = (istanzeBGL['Tupla']==t)
        istanze_filtrate = istanzeBGL.loc[mask]
        if (len(istanze_filtrate['Card type'].unique())>1):
            coll_countBGL_cardtype = coll_countBGL_cardtype+1
            print('Collisione -- tupla: '+ str(t))
            collBGL_cardtype[t]=istanze_filtrate['Card type'].unique()
    else:
        print('File finito')
print('Collisioni per diversa tipologia di card: ' + str(coll_countBGL_cardtype))
print (collBGL_cardtype)
#stampo collBGL_cardtype in un file txt andando a capo per ogni elemento della lista

with open('collisioni_BGL_cardtype_per_tipologia.txt', 'w') as f:
    for key, value in collBGL_cardtype.items():
        f.write('%s:%s\n' % (key, value))
f.close()
