# Descripcion: Programa que solicita al usuario por un string y devuelve si la misma es un palindromo o si no lo es
# Entrada: Palabra a
# Salida:  Es palindromo o no es palindromo
# Autor:   EALCALA
# Fecha:  28.04.2017
# Version: 1.0
#Plataforma: Python v3.6


a = input("Introduzca un string para probar si es un palindromo:")

c = list(a) # convierte el string en una lista con cada letra
c.reverse() # invierte los elementos de la lista anterior
l = "".join(c) # convierte la lista invertida anteriormente en un string 
if a == l: # compara el string normal con el string invertido para ver si es o no un palindromo
 print(a, "es un palindromo")
else:
 print(a, "no es un palindromo")








 

  
