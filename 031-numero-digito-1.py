# Leer un número entero y determinar cuántas veces tiene el dígito 1.

number = int(input("Ingrese un numero entero "))
conta = 0
dig = 0
while number != 0:
    dig = number % 10
    number = int(number / 10)
    if dig == 1:       
        conta = int(conta + 1)
print(f"El numero ingresado tiene {conta}  digito uno")
 