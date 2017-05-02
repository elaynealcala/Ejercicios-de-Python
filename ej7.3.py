# Descripción: Programa que, de una lista precargada [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], escoge los numeros pares y los imprime de salida en una lista al usuario en una sola linea
# Entrada: Lista [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Salida:  Una lista que contiene los numeros pares de la lista [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Autor:   EALCALA
# Fecha:  01.05.2017
# Version: 3.0
#Plataforma: Python v3.6


print(list(n for n in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if n%2==0))
