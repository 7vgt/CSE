import random

the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

guesses = 10

star_bank = ["********** *****", "**** *** *******", "***** ******", "********* ******", "****** *****", "***** ****",
             "** *** **** *** ***", "******** *******", "*********", "**********"]

letters_guessed = ["abcdefghijklmnopqrstuvwxyz"]

word_bank = ["futuristic house", "milk and cookies", "snowy forest", "boomerang effect","spooky house","video game",
             "do you know the way","raindrop droptop","jellyfish","thirtyvirus"]

item = random.choice(word_bank)

if the_count[1] == star_bank:
    print("You guessed the word, Congratulations YOU WIN!!!")


if word_bank == star_bank:




  if letters_guessed = word_bank[1]:


while guesses > 0:
        guess = int(input("Guess: "))
        guesses -= 1
