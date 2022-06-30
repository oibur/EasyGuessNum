import random

def computer_guess(x):
    guesses = 0
    low = 1
    high = x
    secret_number = int(input(f'Please choose a number between 1 and {high}: '))
    guess = ''
    while guess != secret_number:
        guess = random.randint(low, high)
        if guess < secret_number:
            low = guess
        else:
            high = guess
        guesses += 1
    print(f'Yay! The computer guessed your number, {guess}, in {guesses} guesses!')

computer_guess(1000000)