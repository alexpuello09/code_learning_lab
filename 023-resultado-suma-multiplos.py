# Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.

suma = 0
conta = 0
multiplo = 3
while conta < 20:
    suma  = suma + multiplo
    multiplo = multiplo + 3
    conta = conta + 1
print(f"\n La suma de los primeros 20 multiplos de 3 es igual a {suma}\n")
