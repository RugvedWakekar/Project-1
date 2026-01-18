import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
lives = 6
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in chosen_word:
    placeholder += "_"
print("Word to guess: " +placeholder)

correct_list = []
game_over = False
while not game_over:
    display = ""
    print(f"****************************<???> /{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ")
    if guess in correct_list:
        print("You have already guessed" +guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_list.append(letter)
        elif letter in correct_list:
            display += letter
        else:
            display += "_"
    print("Word to guess: " +display)

    if guess not in chosen_word:
        lives -= 1
        print("You guessed "+guess+", that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print("****************************YOU LOSE****************************\nThe correct word is "+chosen_word)

    if "_" not in display:
        game_over = True
        print("You Win")
        print("****************************YOU WIN****************************")

    print(stages[lives])