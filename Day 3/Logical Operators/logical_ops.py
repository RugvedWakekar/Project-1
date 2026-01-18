print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("Enter your age: \n"))
    if age < 12:
        bill += 5
        print("child ticket is 5$")
    elif age <= 18:
        bill += 7
        print("youth ticket is 7$")
    elif age <= 45:
        bill += 12
        print("adult ticket is 12")
    elif age >= 45 or age <= 55:
        bill += 0
        print("senior citizen tickets is free")

    photo = input("do you want a photo. type 'y' for yes or 'n' for no: ").lower()
    if photo == 'y':
        bill += 3
    if age >= 45 or age <= 55:
        bill += 0


else:
    print("you cannot ride rollercoaster ")

print(f"your final bill is {bill}")
