def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


def calculator():
    print("=== Intermediate Python Calculator ===")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("0. Exit")

    while True:
        try:
            choice = int(input("\nEnter operation number: "))

            if choice == 0:
                print("Calculator exited.")
                break

            if choice not in range(1, 7):
                print("Invalid choice. Try again.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))
            elif choice == 5:
                print("Result:", power(num1, num2))
            elif choice == 6:
                print("Result:", modulus(num1, num2))

        except ValueError:
            print("Invalid input. Please enter numbers only.")


calculator()
print("end")
print("hello")
