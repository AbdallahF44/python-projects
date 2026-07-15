from operations import add, subtract, multiply, divide, power, modulus

first_loop = 0
while True:
    if first_loop:
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != "y":
            print("Exiting the calculator. Goodbye!")
            break
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(
        "-------\nEnter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter 5 for power\nEnter 6 for modulus\n-------"
    )
    ch = int(input("Enter your choice: "))
    if ch == 1:
        r_add = add(x, y)
        print(f"Addition: {r_add}")
    elif ch == 2:
        r_subtract = subtract(x, y)
        print(f"Subtraction: {r_subtract}")
    elif ch == 3:
        r_multiply = multiply(x, y)
        print(f"Multiplication: {r_multiply}")
    elif ch == 4:
        e_divide = divide(x, y)
        if type(e_divide) == str:
            print(e_divide)
        else:
            print(f"Division: {e_divide}")
    elif ch == 5:
        r_power = power(x, y)
        print(f"Power: {r_power}")
    elif ch == 6:
        e_modulus = modulus(x, y)
        if type(e_modulus) == str:
            print(e_modulus)
        else:
            print(f"Modulus: {e_modulus}")
    else:
        print("Invalid choice. Please try again.")

    print("-" * 30)
    first_loop += 1
