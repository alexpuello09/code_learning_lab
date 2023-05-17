#leer tres numeros y determinar si el ultimo digito de los tres numeros es igual.
entrada1=input("Ingrese un numero entero ")
entrada2=input("Ingrese otro numero entero ")
entrada3=input("Ingrese un ultimo  numero entero ")
num1 = int(entrada1)
num2 = int(entrada2)
num3 = int(entrada3)
num1 = num1%10
num2 = num2%10
num3 = num3%10
if num1 == num2 and num2 == num3:
    print(" ")
    print(f"-Los ultimos digitos de los tres numeros son iguales")
else:
    print(" ")
    print("-Los ultimos digitos de los tres numeros no son iguales")

