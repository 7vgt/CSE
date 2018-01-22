import random
import string


"""

A General Guide for HangMan
1. Make a word Bank- 10 items
2.pick a random item form the list
3.hide the word (use *)
4.Receal letters already guessed
5.create the win condition

"""

the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

word_bank = ["futuristic house", "milk and cookies", "snowy forest", "boomerang","spooky house","video games",
             "do you know the way","raindrop","jellyfish","thirtyvirus"]
item = random.choice(word_bank)
print(item)

guess = int(input("Guess: "))