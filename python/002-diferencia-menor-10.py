entrada1=input("Digite un numero entero ")
entrada2=input("Digite otro numero entero ")
num1=int(entrada1)
num2=int(entrada2)
difer=0
comp=0
if num1 != num2:
    if num1 > num2:
        difer = num1 - num2
        if difer <= 10:
            while num2 < num1 - 1 :
                num2 = num2 + 1
                comp = num2
                print("  ")
                print(comp)
        else:
            print("-Ejecucion finalizada")
    else:
        if num2 > num1:
            difer = num2 - num1 -1
            if difer <= 10:
                while num1 < num2 - 1 :
                    num1 = num1 + 1
                    comp = num1
                    print("  ")
                    print(comp)
            else:
                print("Ejecucion finalizada")
else:
    print("-Los numeros deben ser diferentes")            
