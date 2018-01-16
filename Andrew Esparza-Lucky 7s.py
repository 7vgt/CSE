import random

print("welcome to lucky 7's")

print("lets get started")

highest_round = 0

rounds = 0

money = 15

while money > 0:

    dice1 = random.randint(1, 6)

    dice2 = random.randint(1, 6)

    if (dice1 + dice2) == 7:
        money += 4
        print("you won, you win 4 dollar")
        rounds = rounds + 1

    if (dice1 + dice2) != 7:
        money -= 1
        print("you have fallen, you loose 1 dollar")
        rounds = rounds + 1

print("You have lost all your money get outa here")

print("You played %s rounds" % rounds)
