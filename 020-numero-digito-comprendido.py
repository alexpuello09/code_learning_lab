#Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos 
#entre un dígito y otro.

num = int(input("\nIngrese un numero de dos digitos "))
a = 0
b = 0
if num < 0:
        num = num * (-1)
if num < 100 and num > 9:
    a = int(num/10)
    b = num % 10
    if a == b or a == b + 1 or b == a +1:
        print("\nNo hay numeros comprendidos entre el primer digito y el segundo digito")
    elif a > b:
        print("\nLos numeros comprendidos entre el primer y el segundo digito son :\n")
        for x in range(b + 1,a):
            print(x)
    else:
        print("Los numeros comprendidos entre el segundo y el primer digito son \n")
        for x in range(a + 1,b):
            print(x)
else:
    print("\nEl numero ingresado no es de dos digitos")