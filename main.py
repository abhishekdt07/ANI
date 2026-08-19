import os

from core.brain import ANIBrain
from memory.memory import ANIMemory
from tools.calculator import try_calculate


# AURA project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")


def main():
    print("Hi ABHI, I am ANI.")
    print("Type 'exit' to close me.")

    # -------------------------
    # MEMORY
    # -------------------------

    memory = ANIMemory(MEMORY_FILE)

    # -------------------------
    # BRAIN
    # -------------------------

    brain = ANIBrain(memory.get_all())

    # -------------------------
    # MAIN LOOP
    # -------------------------

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("ANI: Goodbye, sir.")
            break

        if not user_input:
            continue

        # -------------------------
        # REMEMBER
        # -------------------------

        lower_input = user_input.lower()

        if lower_input.startswith("remember"):
            information = user_input[len("remember"):].strip()

            if information:
                memory.remember(information)

                print("ANI: Got it, sir. I'll remember that.")

                # Give the updated memory to the brain
                brain = ANIBrain(memory.get_all())

                continue

        # -------------------------
        # CALCULATOR
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