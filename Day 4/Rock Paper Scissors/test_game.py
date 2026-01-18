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
choice = [rock, paper, scissors]
user_input = int(input("Type, What do you want to play. Type 0 for rock, 1 for paper or 2 for scissors: \n"))
if user_input >= 0 or user_input >= 2:
    print(choice[user_input])

computer_choice = random.randint(0,2)
print("computer chooses: ")
print(choice[computer_choice])

if user_input >= 3 or user_input < 0:
    print("Invalid Input. You lose! ")
elif user_input == 0 and computer_choice == 2:
    print("You Won! ")
elif user_input == 0 and computer_choice == 1:
    print("You Lost! ")
elif user_input == 1 and computer_choice == 0:
    print("You Won! ")
elif user_input == 1 and computer_choice == 2:
    print("You Lost! ")
elif user_input == 2 and computer_choice == 1:
    print("You Won! ")
elif user_input == 2 and computer_choice == 0:
    print("You Lost! ")
elif user_input == computer_choice:
    print("It's a draw! ")
