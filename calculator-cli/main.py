from operations import add, subtract, multiply, divide, power, modulus

operations = {1: add, 2: subtract, 3: multiply, 4: divide, 5: power, 6: modulus}
while True:

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue
    print("""---------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Modulus
7. Exit
---------""")
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
        print("-" * 30)
        continue
    if ch == 7:
        print("Exiting the calculator. Goodbye!")
        print("-" * 30)
        break
    if ch not in operations:
        print("Invalid choice. Please select a valid operation.")
        print("-" * 30)
        continue
    try:
        result = operations.get(ch)(x, y)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)

    print("-" * 30)
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        print("Exiting the calculator. Goodbye!")
        print("-" * 30)
        break
