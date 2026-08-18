import re


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


def try_calculate(user_input):
    """
    Detect simple calculations such as:

    25 + 5
    100 - 40
    12 * 8
    100 / 4
    """

    pattern = (
        r"^\s*(-?\d+(?:\.\d+)?)"
        r"\s*([+\-*/])\s*"
        r"(-?\d+(?:\.\d+)?)\s*$"
    )

    match = re.match(pattern, user_input)

    if not match:
        return None

    a = float(match.group(1))
    operator = match.group(2)
    b = float(match.group(3))

    result = calculate(a, operator, b)

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result


if __name__ == "__main__":
    print("ANI Calculator Tool")

    print(calculate(10, "+", 5))
    print(calculate(10, "-", 5))
    print(calculate(10, "*", 5))
    print(calculate(10, "/", 5))