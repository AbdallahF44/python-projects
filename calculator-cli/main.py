from operations import add, subtract, multiply, divide

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

result_add = add(x, y)
result_subtract = subtract(x, y)
result_multiply = multiply(x, y)
result_divide = divide(x, y)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
if isinstance(result_divide, str):
    print(result_divide)
else:
    print(f"Division: {result_divide}")
