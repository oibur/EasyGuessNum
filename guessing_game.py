import random

def main():
    user_input = int(input("Please enter a number. \n 0. To quit. \n 1. The computer guesses your number \n 2. You guess the computers number \n"))
    while user_input != 0:
        if user_input == 1:
            comp_guesses()
        elif user_input == 2:
            user_guesses()
        user_input = int(input("Please enter a number. \n 0. To quit. \n 1. The computer guesses your number \n 2. You guess the computers number \n"))

def comp_guesses():
    guess = 0
    number_guesses = 0
    user_number = int(input("Please enter a number between 1 and 1000 to be guessed: "))
    while guess != user_number:
        print(guess)
        guess = random.randint(1, 1000)
        number_guesses += 1
    print(f'Your number was {guess}, it took {number_guesses} guesses')

def user_guesses():
    secret_number = random.randint(1, 99)
    number_guesses = 0
    print("I am thinking of a number between 1 and 99...")
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        # True if guess is less than secret number
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print("") # an empty line
        guess = int(input("Enter a new guess: "))
        number_guesses += 1
    print(f'Congrats! The number was: {secret_number}, it took you {number_guesses} guesses')

if __name__ == '__main__':
    main()