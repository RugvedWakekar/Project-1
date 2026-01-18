rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
user_side = [rock, paper, scissors]
user_input = int(input("Type what do you want to play. Type 0 for Rock, 1 for Peper or 2 for Scissors: \n"))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Oops, Type valid Input")
#if user_input >= 0 and user_input <= 2:
#print(user_side[user_input])
#else:
#print("Invalid input")

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(user_side[computer_choice])

if user_input < 3 or user_input >= 0:

    if user_input == 0 and computer_choice == 1:
        print("You Lost!")
    elif user_input == 0 and computer_choice == 2:
        print("You Won!")
    elif user_input == 1 and computer_choice == 0:
        print("You Won!")
    elif user_input == 1 and computer_choice == 2:
        print("You Lost!")
    elif user_input == 2 and computer_choice == 0:
        print("You Won!")
    elif user_input == 2 and computer_choice == 1:
        print("You Lost!")
    elif user_input == computer_choice:
        print("It's a draw!")
else:
    print("Invalid input, You lose!! ")
