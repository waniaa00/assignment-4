import random 

def main():
    secret_number = random.randint(1, 99)

    print("Guess what number I'm thinking of — it's somewhere between 1 and 99..")

    guess = int(input("Enter a guess:  "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")
        
        print()
        guess = int(input("Enter a new guess: "))

    print(f"Congrats! You guessed the number right, it was {secret_number}")


if __name__ == '__main__':
    main()