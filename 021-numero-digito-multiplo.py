#  Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído. 
num = int(input("Ingrese un numero entero "))
if num < 0:
    num = num*(-1)
print("\nLos multiplos de 5 entre 1 y el numero ingresado son :")
for x in range(1 +1,num):
    if x % 10 == 0 or x % 10 == 5:
        print(x)





