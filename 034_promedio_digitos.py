#  Leer un número entero y determinar a cuánto es igual al suma de sus dígitos pares. 

number = int(input("\nIngrese un número entero "))
suma = 0
ult_dig = 0
promedio = 0
conta = 0
if number < 0:
    number = number * (-1)

while number != 0:
    ult_dig = number % 10
    conta += 1
    suma += ult_dig
    number = number // 10
    
promedio = suma / conta
print(f"\nEl promedio de los digitos es igual a {round(promedio)}\n")
