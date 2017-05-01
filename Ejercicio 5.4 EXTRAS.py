# Descripción: Programa que devuelve una lista que contiene solo los elementos que son comunes entre dos listas de distintos tamanos generadas aleatoriamente (sin duplicados)
# Entrada: Listas generadas aleatoriamente por el programa
# Salida:  Lista de elementos comunes entre ambas listas
# Autor:   EALCALA
# Fecha:  27.04.2017
# Version: 4.0
#Plataforma: Python v3.6

import random
a = []
b = []
for i in range(0,10):
 a.append(random.randint(0,100))

for j in range(0,20):
 b.append(random.randint(0,100))

print (list(set(a) & (set(b))))





 

  
