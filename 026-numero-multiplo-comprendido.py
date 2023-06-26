#  Leer dos números entero y mostrar todos los múltiplos de 5 comprendidos entre el menor y el 
# mayor. 

num1 = int(input("Ingrese un número entero "))
num2 = int(input("Ingrese otro número entero "))

if num1 < 0:
    num1 = -num1
if num2 < 0:
    num2 = -num2
if num1 > num2:
    menor = num2
    mayor = num1
else:
    menor = num1
    mayor = num2
print("\nEstos son los multiplos de 5 comprendidos entre el menor y el mayor :")
while menor <= mayor:
    menor = menor + 1
    multiplo = menor
    if multiplo % 5 == 0:
        print(multiplo)
        