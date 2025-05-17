# Step 1
def main():
    # print("This program adds two numbers.")

    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)

    num2 : str = input("Enter second number: ")
    num2 : int = int(num2)

    total : int = num1 + num2
    # print("The total is " + str(total) + ".")

# if __name__ == '__main__':
#     main()

# Step 2
def sum():
    print("This program adds two numbers.")

    sum1 = int(input("Enter first number: "))

    sum2 = int(input("Enter second number: "))

    totalSum = sum1 + sum2

    print(f"The total is {totalSum}.")

sum()
