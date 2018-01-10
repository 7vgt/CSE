import random

guesses = 5

number = random.randint(0, 50)

win = False

while guesses > 0:
    guess = int(input("Guess: "))

    guesses -= 1

    if guess > number:
        print("Too High", guesses, "remaining")
    elif guess < number:
        print("Too Low", guesses, "remaining")
    elif guess - number < 6:
        print("You are very close")
    else:
        print("Congrats, you Won The game")
        win = True
        guesses = 0

if win == False:
    print("Sorry,Try Again Next Time", number)