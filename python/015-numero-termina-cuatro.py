#Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos. 

num1 = input("Ingrese un numero entero :")
num2 = input("Ingrese otro numero entero :")
num1 = int(num1)
num2 = int(num2)
if num1 < num2:
    for x in range(num1 + 1,num2):
        if x %  10 == 4:
            print(x)
elif num1 > num2:
    for x in range(num2 + 1,num1):
        if x % 10 == 4:
            print(x)

else:
    print ("Los numeros ingresados deben ser diferentes")

