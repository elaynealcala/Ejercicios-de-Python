# Descripcion: Este programa pide a un usuario adivinar un numero entre el 1 y el 9, ambos incluidos
# Entrada: Numero entre el uno y el nueve
# Salida:  El numero es mayor, menor o igual
# Autor:   EALCALA
# Fecha:  04.05.2017
# Version: 2.0
#Plataforma: Python v2.7

import random
a = int(random.randrange(1, 9))
n = 0
c = 0
while n != a and n != "F":
 n = input("Adivine un numero entre el 1 y el 9, ambos incluidos, o teclee F para salir: ")

 if n == F:
  break

 try:
  n = int(n)
 except ValueError:
  print("El valor no es un numero")

 c += 1

 if n>a:
  print("su numero es mayor al escogido!")
 elif n<a:
  print("su numero es menor al elegido")
 else:
  print("Felicidades, usted ha adivinado!")
  print("numero de intentos")
  print c
