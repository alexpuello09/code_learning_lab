# Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

num = int(input("\nIngrese un numero de tres dígitos "))
num_dig = 0
if num < 0:
    num = num * (-1)
if num < 1000 and num > 99:

    while num != 0:
        num_dig = num % 10
        num = int(num / 10)
        if num_dig == 1:
            print("\nEl numero ingresado contiene el digito 1")
else:
    print("\nEl numero ingresado no es de tres digitos\n")
