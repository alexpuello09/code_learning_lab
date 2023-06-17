# Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205

a = 25
b = 205
for x in range(25,205):
    if x % 10 == 6:
        print(x)