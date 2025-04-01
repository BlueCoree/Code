ef add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by Zero."
    return x / y

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Existing calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"result: {add(num1, num2)}")
            elif choice == '2':
                print(f"result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"result: {multiply(num1,num2)}")
            elif choice == '4':
                print(f"result: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please select a valid option.")
