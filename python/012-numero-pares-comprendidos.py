#Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído. 

num = input("Digite un numero entero ")
num = int(num)
numInicial = 2
print("Los numeros pares comprendidos entre 1 y el numero digitado son ")
while numInicial <= num:
    print(numInicial)
    numInicial = numInicial + 2

