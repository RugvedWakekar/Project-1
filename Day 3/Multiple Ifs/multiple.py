print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age <= 12:
        bill += 5
    elif age >= 12 and age < 18:
        bill += 7
    else:
        bill += 12
    photo = input("do you want a picture while you ride? Press 'y' for yes or 'n' for no: \n")
    if photo == 'y':
        bill += 3
        print(f"Your final bill is : {bill}$")
    else:
        print(f"your final bill is : {bill}$")
else:
    print("you cannot ride the rollercoaster")