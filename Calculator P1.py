def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


def power(x, y):
    return x ** y


def modulo(x, y):
    if y == 0:
        return "Error: Modulo by zero!"
    return x % y


def square_root(x):
    if x < 0:
        return "Error: Square root of negative number!"
    return x ** 0.5


def display_menu():
    print("\n" + "=" * 40)
    print("           CALCULATOR MENU")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulo (%)")
    print("7. Square Root (√)")
    print("8. Exit")
    print("=" * 40)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Invalid choice! Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 8:
            print("\nThank you for using the calculator! Goodbye!")
            break

        if choice == 7:  # Square root only needs one number
            num = get_number("Enter a number: ")
            result = square_root(num)
            print(f"\n√{num} = {result}")
        else:
            # Operations that need two numbers
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == 1:
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            elif choice == 5:
                result = power(num1, num2)
                print(f"\n{num1} ** {num2} = {result}")
            elif choice == 6:
                result = modulo(num1, num2)
                print(f"\n{num1} % {num2} = {result}")

        # Ask if user wants to continue
        while True:
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower()
            if continue_calc in ['y', 'yes']:
                break
            elif continue_calc in ['n', 'no']:
                print("\nThank you for using the calculator! Goodbye!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")


# Run the calculator
if __name__ == "__main__":
    calculator()