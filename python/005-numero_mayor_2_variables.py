#Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables

entrada1=input("Digite un numero entero ")
num = int(entrada1)
mayor = 0
if num > mayor:
    mayor = num
    print(" ")
entrada2=input("Digite otro numero entero ")
num = int(entrada2)
if num > mayor:
    mayor = num
print(" ")
entrada3=input("Digite un ultimo numero entero ")
num = int(entrada3)
if num > mayor:
    mayor = num
print(" ")
print(f"-El mayor de los numeros digitados es el {mayor}")
