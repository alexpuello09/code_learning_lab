
number = int(input("Ingrese un numero entero "))

number_div = 0
for number_div in range(1,number):

    if number_div % 3 == 0 and number_div % 5 == 0:
        print("FizzBuzz")
    if number_div % 3 == 0:
        print("Fizz")
    elif number_div % 5 == 0:
        print("Buzz")
    else:
        print(number_div)