#Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos.

number_one = len(input("ingrese un numero entero "))
number_two = len(input("ingrese otro numero entero "))

if number_one > number_two:
    print("\tEl primer numero tiene ingresado mas digitos que el segundo  \n")
elif number_two > number_one:
    print("\tEl segundo numero tiene ingresado mas digitos que el primero \n")
else:
    print("\tLos numeros digitados tienen la misma cantidad de digitos \n")