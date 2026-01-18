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
print("computer chose: ")
machine_input = random.randint(0,2)
print(user_side[machine_input])

if user_input >= 3 or user_input < 0:
    print("invalid input")
elif user_input == 0 and machine_input == 1:
    print("you lose")
elif user_input == 1 and machine_input == 2:
    print("you lose")
elif user_input == 2 and machine_input == 0:
    print("you lose")
elif user_input == 0 and machine_input == 2:
    print("you win")
elif user_input == 1 and machine_input == 0:
    print("you win")
elif user_input == 2 and machine_input == 1:
    print("you win")
elif user_input == machine_input:
    print("It is a draw")