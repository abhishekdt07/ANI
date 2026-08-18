def calculate(a, operator, b):
    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero."
        return a / b

    else:
        return "Unknown operator."


if __name__ == "__main__":
    print("ANI Calculator Tool")

    print(calculate(10, "+", 5))
    print(calculate(10, "-", 5))
    print(calculate(10, "*", 5))
    print(calculate(10, "/", 5))