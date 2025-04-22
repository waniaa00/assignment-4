import random 

NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100


def main():
    
       values = [random.randint(MIN_VALUE,MAX_VALUE) for _ in range(NUMBERS)]
       print(f"The {NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE} are: {values}")


if __name__ == "__main__":
    main()