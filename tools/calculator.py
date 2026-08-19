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


def clean_number(value):
    number = float(value)

    if number.is_integer():
        return int(number)

    return number


def try_calculate(user_input):
    """
    Understand both mathematical expressions and
    simple natural-language calculations.

    Examples:

    25 + 5
    100 / 4
    calculate 89 times 326
    988 divided by 5
    add 25 and 50
    subtract 10 from 30
    """

    text = user_input.lower().strip()

    # Remove common ANI phrases
    text = re.sub(r"\bani\b[,:\s]*", "", text)
    text = text.strip()

    # --------------------------------
    # DIRECT MATHEMATICAL EXPRESSION
    # --------------------------------

    pattern = (
        r"^\s*(-?\d+(?:\.\d+)?)"
        r"\s*([+\-*/])\s*"
        r"(-?\d+(?:\.\d+)?)\s*$"
    )

    match = re.match(pattern, text)

    if match:
        a = clean_number(match.group(1))
        operator = match.group(2)
        b = clean_number(match.group(3))

        return calculate(a, operator, b)

    # --------------------------------
    # NATURAL LANGUAGE
    # --------------------------------

    text = text.replace("what is", "")
    text = text.replace("calculate", "")
    text = text.replace("please", "")
    text = text.strip()

    # multiplication
    pattern = (
        r"(-?\d+(?:\.\d+)?)"
        r"\s*(?:times|multiplied by|multiply)"
        r"\s*(-?\d+(?:\.\d+)?)"
    )

    match = re.search(pattern, text)

    if match:
        a = clean_number(match.group(1))
        b = clean_number(match.group(2))

        return calculate(a, "*", b)

    # division
    pattern = (
        r"(-?\d+(?:\.\d+)?)"
        r"\s*(?:divided by|divide by)"
        r"\s*(-?\d+(?:\.\d+)?)"
    )

    match = re.search(pattern, text)

    if match:
        a = clean_number(match.group(1))
        b = clean_number(match.group(2))

        return calculate(a, "/", b)

    # addition
    pattern = (
        r"(-?\d+(?:\.\d+)?)"
        r"\s*(?:plus|add)"
        r"\s*(-?\d+(?:\.\d+)?)"
    )

    match = re.search(pattern, text)

    if match:
        a = clean_number(match.group(1))
        b = clean_number(match.group(2))

        return calculate(a, "+", b)

    # subtraction
    pattern = (
        r"(-?\d+(?:\.\d+)?)"
        r"\s*(?:minus|subtract)"
        r"\s*(-?\d+(?:\.\d+)?)"
    )

    match = re.search(pattern, text)

    if match:
        a = clean_number(match.group(1))
        b = clean_number(match.group(2))

        return calculate(a, "-", b)

    return None


if __name__ == "__main__":
    print("ANI Calculator Tool")

    print(calculate(10, "+", 5))
    print(calculate(10, "-", 5))
    print(calculate(10, "*", 5))
    print(calculate(10, "/", 5))