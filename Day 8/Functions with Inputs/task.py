def life_in_weeks():
    calculated_age = 90 - age
    left_weeks = float(calculated_age * 52.1429)
    round_weeks = round(left_weeks, 2)
    print(f"You have {round_weeks} weeks left.")

age = int(input("Enter your age: "))
life_in_weeks()


