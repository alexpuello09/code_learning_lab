
import random
repeat = "yes"
print("\nWelcome to the Dice Rolling Simulator!\n")
    
while repeat.lower() == "yes":
    repeat = "a"
    while repeat.lower() != "yes" and repeat.lower() != "no":
        roll = (input("Roll the dice? yes/no : "))
        repeat = roll.lower()

        if repeat.lower() == "yes":
            number = random.randint(1,6)
            print(f"\nResult : {number}")

        if repeat.lower() == "no":
            print("Programa finalizado\n")

        elif repeat.lower() != "yes" and repeat.lower != "no":
            print("Invalid input try again \n")