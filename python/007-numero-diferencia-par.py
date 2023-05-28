#Leer dos números enteros y si la diferencia entre los dos números es par mostrar en pantalla la 
#suma de los dígitos de los números, si dicha diferencia es un número primo menor que 10 
#entonces mostrar en pantalla el producto de los dos números y si la diferencia entre ellos 
#terminar en 4 mostrar en pantalla todos los dígitos por separado.


entrada1 = input("Digite un número entero ")
entrada2 = input("Digite otro número entero ")
num1 = int(entrada1)
num2 = int(entrada2)
ultimodig1 = 0
ultimodig2 = 0
sumadigs = 0
difer = 0
producto = 0
suma1 = 0
suma2 = 0
ultimodig = 0

if num1 < 0:
    num1 = num1 * (-1)
if num2 < 0:
    num2 = num2 * (-1)

if num1 != num2:
    if num1 > num2:
        difer = num1 - num2
    if num2 > num1:
        difer = num2 - num1

    if difer % 2 == 0:
        while num1 != 0:
            ultimodig1 = num1 % 10
            suma1 = suma1 + ultimodig1
            num1 = num1 // 10

        while num2 != 0:
            ultimodig2 = num2 % 10
            suma2 = suma2 + ultimodig2
            num2 = num2 // 10
        sumadigs = suma1 + suma2
        print(" ")
        print(f"-La suma de todos los dígitos es {sumadigs}")
        print(" ")

    if difer % 2 != 0 and difer < 10:
        producto = num1 * num2
        print(" ")
        print(f"-El producto de los números digitados es {producto}")

    if difer % 10 == 4:
        num1 = int(entrada1)
        num2 = int(entrada2)
        print("-Los digitos de los dos numeros ingresados son:")
        while num1 != 0:
            ultimodig = num1 % 10
            num1 = int(num1/10)
            print(ultimodig)

        while num2 != 0:
            ultimodig = num2 % 10
            num2 = int(num2/10)
            print(ultimodig)
else:
    print("-Los numeros ingresados deben ser diferentes")



