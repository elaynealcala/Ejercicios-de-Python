# Descripción: Programa que, de una lista a precargada, escoge los numeros pares y los imprime de salida en una lista al usuario
# Entrada: Lista a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Salida:  Una lista que contiene los numeros pares de la lista a
# Autor:   EALCALA
# Fecha:  01.05.2017
# Version: 2.0
#Plataforma: Python v3.6


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(n for n in a if n%2==0))
