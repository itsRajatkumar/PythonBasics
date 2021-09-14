import random

print('Rock - Paper - Scissor')

n=10
options = ['r', 'p', 's']
rounds = 1
comp_win = 0
user_win = 0

while rounds <= n:
    print(f"\n----Round :{rounds} ----\nRock -   'r'\nPaper -  'p'\nScissor - 's'")
    player = input("Chose your option: ")

    if player != 'r' and player != 'p' and player != 's':
        print("Invalid input, try again\n")
        continue
    computer = random.choice(options)

    if computer == 'r':

        if player == 's':
            comp_win=comp_win+1

        elif player == 'p':
            user_win=user_win+1

    elif computer == 'p':

        if player == 'r':
            comp_win=comp_win+1

        elif player == 's':
            user_win=user_win+1

    elif computer == 's':

        if player == 'p':
            comp_win=comp_win+1

        elif player == 'r':
            user_win=user_win+1

    if user_win > comp_win:
        print(f"You Won round {rounds}\n")

    elif comp_win > user_win:
        print(f"Computer Won round {rounds}\n")

    else:
        print("Draw!!\n")
    rounds += 1

if user_win > comp_win:
    print("\nCongratulations!! You Won")

elif comp_win > user_win:
    print("\nYou lose!!")

else:
    print("\nMatch Draw!!")