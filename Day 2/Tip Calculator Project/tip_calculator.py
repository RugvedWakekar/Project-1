print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, 15? "))
people = float(input("How many people to spilt the bill? "))
percentage = (tip/100 * bill) + bill
difference = percentage / people
rounding = round(difference, 2)
print(f"Each person have to pay: {rounding}")
