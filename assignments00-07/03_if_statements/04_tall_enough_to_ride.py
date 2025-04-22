MINIMUM_HEIGHT = 50

def main():
    height = float(input("Enter your height(in cm):"))
    if height >= MINIMUM_HEIGHT:
        print("You've got the height, let's ride!")
    else:
        print("So close! Grow a little more and come back next year.")



if __name__ == "__main__":
    main()