def double(num: int):
    return num * 2

def main():
    num = int(input("Enter a number: "))
    doubled_number = double(num)
    print(f"Doubled number is : {doubled_number}")


if __name__ == "__main__":
    main()