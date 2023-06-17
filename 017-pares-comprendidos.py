#Mostrar en pantalla todos los pares comprendidos entre 20 y 200:


for x in range(20 + 2,200):
    if int(x/2)*2 == x:
        print(x)
