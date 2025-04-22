def num_in_stock(fruit):
    inventory = {
        "strawberry" : 2,
        " mango" : 4,
        "banana" : 3,
        "kiwi": 5,
        "orange": 6
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip()
    stock = num_in_stock(fruit)

    if stock > 0:
         print(f"This fruit is available! Quantity in stock: {stock} ")
    else:
        print("Out of stock – check back soon!")


if __name__ == '__main__':
    main()
   
