print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("This is robbery, give me 5$ quick: ")
    elif age <= 18:
        print("This is still a robbery, give me 7$ fast: ")
    else:
        print("You look like an adult, give me 12$: ")
else:
    print("Grow some balls to ride this rollercoaster")