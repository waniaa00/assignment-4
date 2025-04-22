def main():
    numbers : list[int] = [1, 2, 3, 4, 5]

    doubled_numbers = [num * 2 for num in numbers]

    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")


if __name__ == '__main__':
    main()