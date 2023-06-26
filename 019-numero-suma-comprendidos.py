#Leer un número entero y determinar a cuánto es igual la suma de todos los enteros 
#comprendidos entre 1 y el número leído. 

numero = int(input("Ingrese un numero entero "))
suma = 0
if numero < 0:
    numero = numero * (-1)
for x in range(2,numero):
    suma = int(suma) + x
print(suma)
