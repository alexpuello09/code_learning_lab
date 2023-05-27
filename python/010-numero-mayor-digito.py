#Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra 
#el mayor dígito.

entrada1 = input("Digite un numero de dos digitos ")
num1 = int(entrada1)
mayordig = 0
posicion = 0
if num1 < 0:
    num1 = num1*(-1)
if num1 > 9 and num1 < 100:
    a = num1 // 10
    b = num1 % 10
    if a > mayordig:
        mayordig =a
        posicion =num1
    if b > mayordig:
        mayordig = b
        posicion = num1


print(" ")
entrada2 = input("Digite otro numero de dos digitos ")
num2= int(entrada2)
if num2 < 0:
    num2 = num2*(-1)
if num2 > 9 and num2 < 100:
    a = num2 // 10
    b = num2 % 10
    if a > mayordig:
        mayordig =a
        posicion =num2
    if b > mayordig:
        mayordig = b
        posicion = num2


print(" ")
entrada3 = input("Digite un ultimo numero de dos digitos ")
num3= int(entrada3)
if num3 < 0:
    num3 = num3 * (-1)
if num3 > 9 and num3 < 100:
    a = num3 // 10
    b = num3 % 10
    if a > mayordig:
        mayordig =a
        posicion =num3
    if b > mayordig:
        mayordig = b
        posicion = num3


    print(" ")
    print(f"-El mayor digito es {mayordig} y esta en el numero {posicion}")


