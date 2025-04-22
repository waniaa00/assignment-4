# HANGMAN GAME
import random

def hangman():
    words = ['python', 'java', 'javascript', 'ruby', 'swift', 'kotlin', 'typescript']
    word_to_guess = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = "".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
        print(f"Word: {display_word}")

        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    else:
        print(f"Game over! The word was '{word_to_guess}'.")

# Run the game
hangman()
