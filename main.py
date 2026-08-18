import json
import os

from core.brain import ANIBrain
from tools.calculator import try_calculate


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
        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )


def main():
    print("Hi ABHI, I am ANI.")
    print("Type 'exit' to close me.")

    memory = load_memory()

    brain = ANIBrain(memory)

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("ANI: Goodbye, sir.")
            break

        if not user_input:
            continue

        # -------------------------
        # MEMORY
        # -------------------------

        lower_input = user_input.lower()

        if lower_input.startswith("remember"):
            memory_text = user_input[len("remember"):].strip()

            if memory_text:
                memory.append(memory_text)
                save_memory(memory)

                print("ANI: Got it, sir. I'll remember that.")

                # Rebuild brain so the new memory is available
                brain = ANIBrain(memory)

                continue

        # -------------------------
        # CALCULATOR TOOL
        # -------------------------

        calculation_result = try_calculate(user_input)

        if calculation_result is not None:
            print(
                f"ANI: The answer is {calculation_result}."
            )
            continue

        # -------------------------
        # AI BRAIN
        # -------------------------

        print("ANI: ", end="", flush=True)

        response = brain.ask(user_input)

        print(response)


if __name__ == "__main__":
    main()