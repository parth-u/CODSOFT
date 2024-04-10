def main():
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user for the operation
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = input("Enter the operation number (1, 2, 3, or 4): ")

    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        print(f"The result is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")

if __name__ == "__main__":
    main()
