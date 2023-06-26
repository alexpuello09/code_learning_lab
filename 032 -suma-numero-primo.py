# . Leer un número entero y determinar si la suma de sus dígitos es también un número primo. 

number = int(input("\nIngrese un numero entero "))
dig = 0
suma = 0
while number != 0:
    dig = number % 10
    suma = int(suma + dig)
    number = int(number/10)
if int(suma/ 2) * 2 == suma:
    print("\nla suma de los digitos no es un numero primo ")
else:
    print("\nLa suma de los digitos es un numero primo")