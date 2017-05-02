# Descripción: Programa  que pregunta al usuario por un numero, imprimiendo en una lista de todos los divisores de este numero. Si la entrada no es numerica da un error
# Entrada: Numero x entero
# Salida:  Numeros que son divisores de x
# Autor:   EALCALA
# Fecha:  26.04.2017
# Version: 2.0
#Plataforma: Python v3.6

x = input("Escoja un numero entero para saber sus divisores: ")

try:
 x = int(x)
except ValueError:
 print("El valor no es un numero")

lista = list(range(1, x+1))
lista2 = []
for number in lista:
 if x%number == 0:
  lista2.append(number)

print(lista2)
