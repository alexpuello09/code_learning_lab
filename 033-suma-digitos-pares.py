#. Leer un número entero y determinar a cuánto es igual al suma de sus dígitos pares. 

number = int(input("Ingrese un número entero "))
suma_digitos_pares = 0

while number > 0:
    digito = number % 10
    if digito % 2 == 0:
        suma_digitos_pares = suma_digitos_pares+ digito
    number = number // 10

print(f"La suma de los digitos pares es {suma_digitos_pares}")
