import random

win = "False"

the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

guesses = 10

letters_guessed = []

word_bank = ["futuristic house", "milk and cookies", "snowy forest", "boomerang","spooky house","video game",
             "do you know the way","raindrop droptop","jellyfish","thirtyvirus"]

word = random.choice(word_bank)

range_of_letters = len(word)

word_selector_stars = range_of_letters * "*"

if word == "futuristic house":
    word_selector_stars = "********** *****"

if word == "milk and cookies":
    word_selector_stars = "**** *** *******"

if word == "snowy forest":
    word_selector_stars = "***** ******"

if word == "spooky house":
    word_selector_stars = "****** *****"

if word == "video game":
    word_selector_stars = "***** ****"

if word == "do you know the way":
        word_selector_stars = "** *** **** *** ***"

if word == "raindrop droptop":
    word_selector_stars = "******** *******"

while guesses > 0:
    print(word_selector_stars)
    print(word)
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    guess = input("Guess: ")
    guesses -= 1
    print(output)
    guess_lowercase = guess.lower()
    letters_guessed.append(guess_lowercase)
    if letters_guessed == word:
        print("you win")
        guess = 0
