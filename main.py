from ollama import chat
import json
import os
import re

# Always keep memory.json inside the AURA project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

    return []


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)


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
    Looks for simple calculations such as:
    25 + 5
    100 - 40
    12 * 8
    100 / 4
    """

    pattern = r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$"

    match = re.match(pattern, user_input)

    if not match:
        return None

    a = float(match.group(1))
    operator = match.group(2)
    b = float(match.group(3))

    result = calculate(a, operator, b)

    # Make whole numbers look cleaner
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result


print("Hi ABHI, I am ANI.")
print("Type 'exit' to close me.")

memory = load_memory()

conversation = [
    {
        "role": "system",
        "content": (
            "Your name is ANI. "
            "You are Abhi's personal AI assistant. "
            "Always identify yourself as ANI, never as Qwen. "
            "Be friendly, helpful, and conversational. "
            "Use conversation history and saved memory when answering. "
            "Do not invent memories."
        )
    }
]


# Load saved memories
if memory:
    memory_text = "\n".join(
        f"- {item}" for item in memory
    )

    conversation.append(
        {
            "role": "system",
            "content": (
                "These are things ANI has saved about Abhi:\n"
                + memory_text
            )
        }
    )


while True:

    user_input = input("You: ").strip()

    # Exit
    if user_input.lower() == "exit":
        print("ANI: Goodbye, sir.")
        break

    # Ignore empty input
    if not user_input:
        continue

    # Save information when the user asks ANI to remember something
    lower_input = user_input.lower()

    if lower_input.startswith("remember"):
        memory_text = user_input[len("remember"):].strip()

        if memory_text:
            memory.append(memory_text)
            save_memory(memory)

            print("ANI: Got it, sir. I'll remember that.")

            conversation.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            conversation.append(
                {
                    "role": "assistant",
                    "content": "Got it, sir. I'll remember that."
                }
            )

            continue

    # Calculator tool
    calculation_result = try_calculate(user_input)

    if calculation_result is not None:
        print(f"ANI: The answer is {calculation_result}.")

        conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        conversation.append(
            {
                "role": "assistant",
                "content": f"The answer is {calculation_result}."
            }
        )

        continue

    # Normal AI conversation
    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    print("ANI: ", end="", flush=True)

    stream = chat(
        model="qwen3:4b",
        messages=conversation,
        stream=True
    )

    assistant_response = ""

    for chunk in stream:
        text = chunk["message"]["content"]

        print(text, end="", flush=True)

        assistant_response += text

    print()

    conversation.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )