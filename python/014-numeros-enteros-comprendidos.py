#Leer dos números y mostrar todos los enteros comprendidos entre ellos

num1 = input("Digite un numero entero ")
num2 = input("Digite otro numero entero ")
num1 = int(num1)
num2 = int(num2)

if num1 < num2:
    for x in range(num1 + 1,num2):
        print(x)
elif num2 < num1:
    for x in range(num2 + 1,num1):
        print(x)
else:
    print("Los numeros digitados son iguales")
