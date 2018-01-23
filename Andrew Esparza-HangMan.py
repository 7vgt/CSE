import random
import string


"""

A General Guide for HangMan
1. Make a word Bank- 10 items
2.pick a random item form the list
3.
4.Receal letters already guessed
5.create the win condition

"""
guess = 10

while guess > 0:

letters_guessed = []

guesses_left =  10

the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

word_bank = ["futuristic house", "milk and cookies", "snowy forest", "boomerang","spooky house","video games",
             "do you know the way","raindrop","jellyfish","thirtyvirus"]

item = random.choice(word_bank)

print(item)

word_bank = list(str1)

if input = word_bank[1]:
   print (word_bank[1])

letters_guessed = (input("Guess: "))
