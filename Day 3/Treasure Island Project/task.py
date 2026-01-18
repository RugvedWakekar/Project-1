print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?\n")
user_input = input('\tType "left" or "right"\n ').lower()

if user_input == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    user_input1 = input('\tType "wait" to wait for a boat. or Type "swim" to swim across.\n').lower()
    if user_input1 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        user_input2 = input('\tOne red, one yellow and one blue. Which door would you choose?\n').lower()
        if user_input2 == "yellow":
            print("You found the treasure! You Win!")
            exit()
        elif user_input2 == "red":
            print("Wrong move! Your greedy ass burned by the room full of fire.")
        elif user_input2 == "blue":
            print("really? You chose blue? whatever, You died bitch.")
        else:
            print("Are you nervous? Type carefully.")
    elif user_input1 == "swim":
        print("Nigga, You know. You can't swim. Then why the fuck did you jump?? ")
    else:
        print("I ain't gonna repeat, type what I say!")

elif user_input == "right":
    print("You cannot always be right, You fell into a hole. Game over.")
else:
    print("you can only use words like 'left' or 'right' ")

