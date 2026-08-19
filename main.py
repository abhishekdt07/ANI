import os

from core.brain import ANIBrain
from core.router import ANIRouter
from memory.memory import ANIMemory
from tools.calculator import try_calculate


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
    # ROUTER
    # -------------------------

    router = ANIRouter(memory, brain)

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
        # ASK ROUTER
        # -------------------------

        route = router.route(user_input)

        # -------------------------
        # MEMORY
        # -------------------------

        if route == "memory_saved":
            print("ANI: Got it, sir. I'll remember that.")

            # Refresh brain with latest memory
            brain = ANIBrain(memory.get_all())
            router.brain = brain

            continue

        # -------------------------
        # CALCULATOR
        # -------------------------

        if route == "calculator":

            result = try_calculate(user_input)

            if result is not None:
                print(f"ANI: The answer is {result}.")
                continue

        # -------------------------
        # AI BRAIN
        # -------------------------

        if route == "brain":

            print("ANI: ", end="", flush=True)

            response = brain.ask(user_input)

            print(response)

            continue

        # -------------------------
        # FALLBACK
        # -------------------------

        print("ANI: I'm not sure how to handle that yet.")


if __name__ == "__main__":
    main()