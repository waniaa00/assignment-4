def main():
    fruits = {"strawberry": 10, "mango": 20, "Kiwi": 15, "pineapple" : 40, "grapes": 30, "chickoo": 18}

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"Enter the quantity of {fruit_name} you want to buy: "))
        total_cost += (price * amount_bought)

    
    print(f"Your total is ${total_cost}.")



if __name__ == "__main__":
    main()
