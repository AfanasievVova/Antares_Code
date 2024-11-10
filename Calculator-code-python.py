def get_multiplication(a, b):
    """multiplies the numbers a/b"""
    return a * b


def get_division(a, b):
    """Divide numbers a / b"""
    return a / b


def get_addition(a, b):
    """Add numbers a + b"""
    return a + b


def get_subtraction(a, b):
    """subtraction a - b numbers"""
    return a - b


def get_squaring(a, b):
    """Multiply by square the numbers a ** b"""
    return a ** b


def calculator(operator, a: float, b: float):
    """The calculator name  function performs calculator operations."""

    if operator == "*":
        return get_multiplication(a, b)
    if operator == "/":
        return get_division(a, b)
    if operator == "+":
        return get_addition(a, b)
    if operator == "-":
        return get_subtraction(a, b)
    if operator == "**":
        return get_squaring(a, b)


operator = input("Add Math Operator: ")
a = float(input("Write a number: "))
b = float(input("Write a number: "))

result = calculator(operator, a, b)
print("Result", result)

