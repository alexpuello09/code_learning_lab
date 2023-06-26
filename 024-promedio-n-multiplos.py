#Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n
#leído. 

n = int(input("\nIngrese un numero entero "))
suma = 0
conta = 0
num = 0
if n < 0:
    n =  n * (-1)
while conta < n:
    conta = conta + 1
    num = num + 3
    suma = suma + num
suma = suma / n
print(f"\nEl promedio de los {n} primeros multiplos de 3 es {suma}\n")








#for x in range(0,n + 1):
   # conta = conta + 1
  #  num = num + 3
 #   suma = num
#print(suma)


    



       