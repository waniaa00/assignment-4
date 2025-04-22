#Guess the Number Game Python Project (user)

import random

def computer_guesses_number():
    lower_bound = 1
    upper_bound = 100
    attempts = 0

    print(f"Think of a number between {lower_bound} and {upper_bound}, and I will try to guess it!")
    input("Press Enter when you're ready...")

    while True:
        guess = (lower_bound + upper_bound) // 2
        attempts += 1

        print(f"Is your number {guess}? (Enter 'h' if too high, 'l' if too low, 'c' if correct)")
        feedback = input().strip().lower()

        if feedback == 'h':
            upper_bound = guess - 1
        elif feedback == 'l':
            lower_bound = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")

# Run the game
computer_guesses_number()
