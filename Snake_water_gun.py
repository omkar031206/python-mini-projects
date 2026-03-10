import random
print("Hello!!\nWelcome to Snake-Water-Gun Game")
print("Press:\n1 for Snake\n2 for Water\n3 for Gun\n0 to quit game")
while True:
    low,high = (1,3)
    num = random.randint(low,high)
    n = int(input("Enter your number:"))
    if n in range(4):
        if n == 0:
            print("Thank you for playing.")
            break
        elif n == 1:
            print("You choose Snake")
            if num == 1:
                print("Both choose Snake.\nIt's a tie")
            elif num == 2:
                print("Bot choose Water.\nSo You win")
            else:
                print("Bot choose Gun.\nSo Bot wins")
        elif n == 2:
            print("You choose Water")
            if num == 1:
                print("Bot choose Snake.\nBot wins")
            elif num == 2:
                print("Both choose Water.\nIt's a tie")
            else:
                print("Bot choose Gun.\nSo You win")
        elif n == 3:
            print("You choose a Gun")
            if num == 1:
                print("Bot choose Snake.\nSo You win")
            elif num == 2:
                print("Bot choose Water.\nSo Bot win")
            else:
                print("Both choose Gun.\nIt's a tie")
    else:
            print("Wrong number!!\nTry Again!!")
'''
import random

game_choices = {1: "Snake", 2: "Water", 3: "Gun"}

print("Hello!!\nWelcome to Snake-Water-Gun Game")
print("Press:\n1 for Snake\n2 for Water\n3 for Gun\n0 to quit game")

while True:
    num = random.randint(1, 3)   # bot choice
    n = int(input("Enter your number: "))

    if n == 0:
        print("Thank you for playing.")
        break

    if n in game_choices:
        print(f"You choose {game_choices[n]}")
        print(f"Bot choose {game_choices[num]}")

        # game logic
        if n == num:
            print("It's a tie")
        elif (n == 1 and num == 2) or (n == 2 and num == 3) or (n == 3 and num == 1):
            print("So You win")
        else:
            print("So Bot wins")
    else:
        print("Wrong number!!\nTry Again!!")
'''            