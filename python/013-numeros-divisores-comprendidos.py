#Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 
#y el número leído.

num = input("Digite  un numero entero ")
num = int(num)
numInicial = 0
if num < 0:
    num = num * (-1)
print("Los divisores exactos entre 1 y el numero digitado son")

while numInicial <= num:
    numInicial = numInicial + 1
    if num % numInicial == 0:
        print(numInicial)

