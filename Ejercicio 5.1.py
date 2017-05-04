# Descripcion: Programa que devuelve una lista que contiene solo los elementos que son comunes entre dos listas de distintos tamanos precargadas (sin duplicados)
# Entrada: Listas precargadas en el programa
# Salida:  Lista de elementos comunes entre ambas listas
# Autor:   EALCALA
# Fecha:  27.04.2017
# Version: 1.0
#Plataforma: Python v3.6


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l = []
for i in a:
 for j in b:
  if i==j:
   l.append(j)

c = set(l)

print (c)








 

  
