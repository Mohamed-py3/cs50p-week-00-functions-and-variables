def main():
#Convert user text input to integers so addition works numerically
    x = int(input("X Equels:"))
    y = int(input("Y Equels:"))
    result = plus_numbers_calculator(x,y)
    print(f"X Plus Y Is {result}")


def plus_numbers_calculator(x,y):
# Return the sum directly so main() decides how to display it
    total = x + y
    return total


main()