#  Leer un número entero y determinar cuál es el mayor de sus dígitos. 

number = int(input("\ningrese un numero entero "))

dig = 0 
mayor = 0
if number < 0:
    number = number * (-2)

while number != 0:
    dig = number - int(number / 10 ) * 10
    number = int(number/10)
    if dig > mayor:
        mayor = dig
print(f"\nEl mayor digito del numero ingresado es {mayor}\n")
