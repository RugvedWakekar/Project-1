import random
import hangman_art
import hangman_words
lives = 6
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("word to guess: " +placeholder)

game_over = False
correct_list = []
while not game_over:
    print(f"****************************{lives}/6 lives left****************************")
    guess = input("Guess a letter: \n").lower()

    if guess in correct_list:
        print("You already guessed this letter: "+guess)
    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_list.append(letter)
        elif letter in correct_list:
            display += guess
        else:
            display += "_"

    print("Word to guess: "+display)

    if guess not in chosen_word:
        lives -= 1
        print("You guessed "+guess+", that's not in the word. You lose a life")
        if lives == 0:
            game_over = False
            print(f"****************************YOU LOSE****************************\nThe correct word was "+chosen_word)

    if "_" not in display:
        game_over = True
        print(f"****************************YOU WIN****************************")

    print(hangman_art.stages[lives])