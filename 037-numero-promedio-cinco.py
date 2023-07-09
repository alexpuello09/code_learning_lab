#Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números 
#terminados en 5.

difer = 1
resultado = 0
conta = 0
promedio = 0
while difer != 0:

    entrada = int(input("Ingrese un numero entero "))
    if entrada < 0:
        entrada = entrada * (-1)
    difer = entrada
    if entrada % 10 == 5:
        resultado += entrada
        conta += 1
promedio = int(resultado / conta)

print(f"El promedio de los numeros terminados en 5 es {promedio}")
