import random

def main():
    user_input = int(input("Please enter a number. \n 0. To quit. \n 1. The computer guesses your number \n 2. You guess the computers number \n"))
    while user_input:
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
        guess = random.randint(1, 1000)
        print(guess)
        number_guesses += 1
    print(f'Your number was {guess}, it took {number_guesses} guesses')

def user_guesses():
    secret_number = random.randint(1, 99)
    user_number = int(input("You have 6 chances to guess my number between 1 and 100: "))
    guesses = 5
    tries = 1
    for i in range(guesses):
        if user_number == secret_number:
            break
        elif user_number > secret_number:
            print("Your number is too high.")
        else:
            print("Your number is too low.")
        user_number = int(input(f'You have {guesses} guesses left: '))
        guesses -= 1
        tries += 1
    if user_number == secret_number:
        print(f'That\'s correct, the number was {secret_number}. You made {tries} guesses.')
    else:
        print(f'Sorry, you did not guess the number was {secret_number}.')

if __name__ == '__main__':
    main()