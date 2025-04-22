#Guess the Number Game Python Project (computer)

import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()

