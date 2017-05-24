# Descripcion: Programa que pide al usuario un numero x y le devuelve de respuesta si el numero es primo o no
# Entrada: Numero x
# Salida:  El numero x es primo o no
# Autor:   EALCALA
# Fecha:  09.05.2017
# Version: 1.0
#Plataforma: Python v2.7

x = int(input("Escoja un numero entero mayor o igual a 2 para saber si es primo o no: "))
x = int(x)

div = [n for n in range(2,x) if x%n == 0]
if len(div) == 0:
    print("el numero es primo")
else:
    print("el numero no es primo")
