def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list.
    once they enter a blank line, break out of the loop amd return the list.
    """

    user_numbers= []
    while True:
        user_input = input("Enter a number:")

        if user_input == "":
            break
        

        num = int(user_input)
        user_numbers.append(num)

    return user_numbers

def count_num(num_list):
    """
    Create an empty dictionary.
    Loop over the list of numbers.
    If the number is not in the dictionary, add it as akey with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """

    num_dict= {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] =1 
        else:
            num_dict[num] += 1
    
    return num_dict

def print_count(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """

    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times")

def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
     
    user_numbers = get_user_numbers()
    num_dict = count_num(user_numbers)
    print_count(num_dict)


if __name__ == "__main__":
    main()
    