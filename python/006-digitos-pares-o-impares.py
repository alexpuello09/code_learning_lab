 #Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares. 

entrada=input("Digite un numero de 4 digitos ")
num = int(entrada)
ultimodig = 0
contapar = 0
contaimpar= 0
if num < 0:
    num = num * (-1)
if num > 999 and num < 9999:
    while num != 0:
        ultimodig = num%10
        num=int(num/10)
        if int(ultimodig/2)*2 == ultimodig:
            contapar = contapar+1
        else:
            contaimpar = contaimpar + 1
    if contaimpar > contapar:
        print(" ")
        print("-El numero digitado tiene mas digitos impares ")
    else:
        if contapar > contaimpar:
            print(" ")
            print("El numero digitado tiene mas digitos pares ")
        else:
            if contapar == contaimpar:
                print(" ")
                print("-El numero digitado tiene la misma cantidad de digitos pares y impares")
else:
    print(" ")
    print("-El numero digitado no es de 4 digitos")

