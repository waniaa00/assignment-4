def main():
    dividend = int(input("\033[1;3m Enter the number to be divided (dividend): \033[0m "))
    divisor  = int(input("\033[1;3m Enter the number to be divided by  (divisor): \033[0m "))

    if divisor == 0:
        print("Division by zero is not allowed.")
        return
    
    quotient = dividend // divisor 
    remainder = dividend % divisor 

    print(f"The result of this division is {quotient} with a remainder of {remainder}")



if __name__ == '__main__':
    main()