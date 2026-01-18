print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
    print("You can ride the rollercoaster! ")
    if age <= 12:
        print("give me 5$")
    elif age >= 12 and age <= 18:
        print("give me 7$")
    else:
        print("give me 12$")
else:
    print("you cannot ride the rollercoaster")