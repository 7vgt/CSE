import random

print("Welcome to Hangman")

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

print(word_selector_stars)

while guesses > 0:
        guess = int(input("Guess: "))
        guesses -= 1
