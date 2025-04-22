def average(x: float, y: float):
    return (x + y) / 2

def main():
    avg1 = average(2, 8)
    avg2 = average(3, 9)

    final_average = average(avg1, avg2)
    print(f"avg1 : {avg1}")
    print(f"avg2 : {avg2} ")
    print(f"final average : {final_average} ")


if __name__ == "__main__":
    main()