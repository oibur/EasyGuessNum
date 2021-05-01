import random

def main():
    comp_guesses()
    we_guess()

def comp_guesses():
    guess = 0
    number_guesses = 0
    user_number = int(input("Please enter a number between 1 and 1000 to be guessed: "))
    while guess != user_number:
        print(guess)
        guess = random.randint(1, 1000)
        number_guesses += 1
    print(f'Your number was {guess}, it took {number_guesses} guesses')

def we_guess():
    secret_number = random.randint(1, 99)
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
    print("Congrats! The number was: " + str(secret_number))

if __name__ == '__main__':
    main()