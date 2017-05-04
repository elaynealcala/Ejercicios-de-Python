# Descripcion: Este programa pide a un usuario adivinar un numero entre el 1 y el 9, ambos incluidos
# Entrada: Numero entre el uno y el nueve
# Salida:  El numero es mayor, menor o igual
# Autor:   EALCALA
# Fecha:  04.05.2017
# Version: 1.0
#Plataforma: Python v2.7

import random

a = int(random.randrange(1, 9))

n = int(input("Adivine un numero entre el 1 y el 9, ambos incluidos: "))

if n>a:
    print("su numero es mayor al escogido!")
elif n<a:
    print("su numero es menor al elegido")
else:
    print("Felicidades, usted ha adivinado! el numero es:")

print a
