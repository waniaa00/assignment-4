MAX_VALUE: int = 100

def main():
    curr_value = int(input("Enter a number you want to double: "))

    while curr_value < MAX_VALUE:
        curr_value = curr_value * 2
        print(curr_value , end= " ")

if __name__ == "__main__":
    main()
