import numpy as np
import pandas as pd
from scipy.stats.mstats import theilslopes
from matplotlib import pyplot as plt


df = pd.read_excel("HomeWork_Regression.xls", sheet_name="VMres3")

print(df)
y = np.array(df["allocated heap"])
x = np.array(df["T(s)"])
slope, intercept, low, up = theilslopes(y, x, 0.95)
print("Pendenza: {} \nIntervallo di confidenza al 95%: [{},{}]  \nIntercetta: {}".format(slope, low, up, intercept))


file = open("Allocated Heap.txt", "w")
file.write("Pendenza: {} \nIntervallo di confidenza al 95%: [{},{}]  \nIntercetta: {}".format(slope, low, up, intercept))
file.close()

#plotto i dati e la retta di regressione

plt.scatter(x, y)
plt.plot(x, slope*x + intercept, color='r')
plt.plot(x, low*x + intercept, color='g')
plt.plot(x, up*x + intercept, color='b')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
