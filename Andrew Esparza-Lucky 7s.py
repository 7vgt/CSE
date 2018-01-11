import random

print("welcome to lucky 7's")

money = 15

while money > 0:

    dice1 = random.randint(1, 6)

    dice2 = random.randint(1, 6)

    if (dice1 + dice2) == 7:
        print("you won, you win $4")
        money += 4

    if (dice1 + dice2) != 7:
        money -= 1





