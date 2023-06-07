#Leer un numero entero y mostrar todos los enteros comprendidos entre 1 y el numero leido.

num = input("Digite un número entero ")
num = int(num)
num1 = 1

print("Los números comprendidos entre 1 y el número digitado son ")
for num1 in range(1, num):
    print(num1)

