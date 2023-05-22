#leer un numero entero de tres digitos y determinar si alguno 
#de sus digitos es igual a la suma de los otros dos

entrada=input("Digite un numeros de tres digitos")
num = int(entrada)
suma = 0
a = 0
b = 0
c = 0
if num < 0:
    num = num * (-1)
if num > 99 and num < 1000 or num > -999 and num < -100:
    c = num - int(num/10)*10
    num = int(num/10)
    b = num%10
    a = int(num/10)
    if c == a + b:
        print(" ")
        print(f"-El tercer digito {c} es igual a la suma de los otros dos digitos")
    else:
        if b == a + c:
            print(" ")
            print(f"-El segundo digito {b} es igual a la suma de los otros dos digitos")
        else:
            if a == b + c:
                print(" ")
                print(f"-El primer digito {a} es igual a la suma de los otros dos digitos")
            else:
                print(" ")
                print("-Ninguno de los tres digitos es igual a la suma de los otros dos")
else:
    print(" ")
    print("-El numero digitado no es de tres digitos")
