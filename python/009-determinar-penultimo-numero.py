#. Leer tres números enteros y determina si el penúltimo dígito de los tres números es igual.

entrada=input("Digite un numero entero ")
print(" ")
num = int(entrada)
penultimo1 = 0
if num > 9:
    penultimo1 = int(num/10)
if num > 99:
    num = int(num/10)
    penultimo1 = num%10


entrada=input("Digite otro numero entero ")
print(" ")
num = int(entrada)
penultimo2 = 0
if num > 9:
    penultimo2 = int(num/10)
if num > 99:
    num = int(num/10)
    penultimo2 = num%10


entrada=input("Digite el ultimo numero entero ")
print(" ")
num = int(entrada)
penultimo3 = 0
if num > 9:
    penultimo3 = int(num/10)
if num > 99:
    num = int(num/10)
    penultimo3 = num%10
if penultimo1 == penultimo2 and penultimo2 == penultimo3:
    print("-Los tres penultimos digitos son iguales")
else:
    print("-Los tres penultimos digitos no son iguales")


