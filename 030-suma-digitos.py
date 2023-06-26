# Leer un número entero y determinar a cuánto es igual al suma de sus dígitos. 

number = int(input("Ingrese un numero entero "))

dig = 0
suma = 0
while number != 0:
    dig = number - int(number/10) * 10
    number = number / 10
    suma = int(suma + dig)
print(f"La suma de los digitos es igual a {suma}")