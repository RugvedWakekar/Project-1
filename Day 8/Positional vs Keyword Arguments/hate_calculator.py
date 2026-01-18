list = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']

def calculate_love_score(male, female):
    for letter in male:
        if letter in list:
            print(letter)

calculate_love_score(male="rugved", female="aditi")


