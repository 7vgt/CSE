print ("welcome to lucky 7's")

import random
number = random.randint(2,12)

round = False

while money > 0:
    money = int(input("Guess:"))

    guesses -=20


if round > money:
    print("you lost 1 dollar")
    else:
        print("Congrats, you Won The game")
        win = True
        round=0

if win == False:
    print("Sorry,Try Again Next Time", number)







