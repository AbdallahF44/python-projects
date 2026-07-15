def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def power(x, y):
    return x**y


def modulus(x, y):
    if y == 0:
        return "Error: Cannot perform modulus by zero"
    return x % y
