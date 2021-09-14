import random

guess = 9

no_of_guesses = 0

_random = random.randint(1,10)

while no_of_guesses < guess:
    _input = int(input('Guesse the Number:'))

    if _input == _random:
        print("You Won \n ")
        break

    elif _input < _random :
        print("Enter Greater Number \n")

    elif _input > _random :
        print("Enter Smaller Number \n")

    else:
        print("you have input wrong \n")

    no_of_guesses = no_of_guesses + 1

    print(f"{guess - no_of_guesses} is left out of {guess} \n")

print("Game over")