# Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para 
#quienes el sea un múltiplo

number = int(input("\nIngrese un numero entero "))
multiplo = 0
contador = 0
print("\nEl numero ingresado es multiplo de: ")
for contador in range(1,number):
    if number % contador == 0:
        print(contador)
    



