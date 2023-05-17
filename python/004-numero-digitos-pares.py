#Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene. 
entrada=input("Ingrese un numero de tres digitos ")
num=int(entrada)
ultimodig=0
contadig=0
if num < 0:
    num = num*(-1)
if num > 99 and num < 1000:
    while num != 0:
        ultimodig = num%10
        num = int(num/10)
        if int(ultimodig/2)*2 == ultimodig:
            contadig = contadig + 1
    print(" ")
    print(f"-El numero ingresado tiene {contadig} digitos pares")
else:
    print(" ")
    print("-El numero ingresado no es de tres digitos ")


