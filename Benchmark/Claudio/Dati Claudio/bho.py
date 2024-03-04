import math
from numpy import var

# I tuoi dati
data = [153772.8, 154693.6, 159744.6, 166718, 163593.8, 169366, 162503.6, 150754.6, 175678.4, 177308.4]

# Calcolo della media
mean = sum(data) / len(data)

# Calcolo della varianza
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Calcolo della deviazione standard
std_dev = math.sqrt(variance)

print(std_dev)

print(mean)

print(math.sqrt(var(data)))

