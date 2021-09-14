import random
print('Snake - Water - Gun')
 
 
# Input no. of rounds
n=10
 
 
# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']
 
# Round numbers
rounds = 1
 
# Count of computer wins
comp_win = 0
 
# Count of player wins
user_win = 0
 
 

while rounds <= n:
 
    # Display round
    print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")
    player = input("Chose your option: ")

    
    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input, try again\n")
        continue

    computer = random.choice(options)
 
    
    if computer == 's':
        if player == 'w':
            comp_win=comp_win+1
        elif player == 'g':
            user_win=user_win+1
 
    elif computer == 'w':
        if player == 'g':
            comp_win=comp_win+1
        elif player == 's':
            user_win=user_win+1
 
    elif computer == 'g':
        if player == 's':
            comp_win=comp_win+1
        elif player == 'w':
            user_win=user_win+1
 
    # Announce winner of every round
    if user_win > comp_win:
        print(f"You Won round {rounds}\n")
    elif comp_win > user_win:
        print(f"Computer Won round {rounds}\n")
    else:
        print("Draw!!\n")
 
    rounds += 1
 
 
# Final winner based on the number of wons
if user_win > comp_win:
    print("Congratulations!! You Won")
elif comp_win > user_win:
    print("You lose!!")
else:
    print("Match Draw!!")