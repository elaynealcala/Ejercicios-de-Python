# Descripcion: Programa que devuelve una lista que contiene solo los elementos que son comunes entre dos listas de distintos tamanos precargadas (sin duplicados)
# Entrada: Listas precargadas en el programa
# Salida:  Lista de elementos comunes entre ambas listas
# Autor:   EALCALA
# Fecha:  08.05.2017
# Version: 2.0
#Plataforma: Python v2.7

import random
a = random.sample(range(1,100), 15)
b = random.sample(range(1,100), 10)
print ([i for i in a if i in b])
