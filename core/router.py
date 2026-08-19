class ANIRouter:
    def __init__(self, memory, brain):
        self.memory = memory
        self.brain = brain

    def route(self, user_input):
        text = user_input.strip()
        lower_text = text.lower()

        # -------------------------
        # MEMORY
        # -------------------------

        if lower_text.startswith("remember"):
            information = text[len("remember"):].strip()

            if information:
                self.memory.remember(information)

                return "memory_saved"

        # -------------------------
        # CALCULATOR
        # -------------------------

        if self.is_calculation(text):
            return "calculator"

        # -------------------------
        # AI BRAIN
        # -------------------------

        return "brain"

    def is_calculation(self, text):
        operators = ["+", "-", "*", "/"]

        # Direct calculation
        if any(operator in text for operator in operators):
            return True

        # Natural language calculation
        calculation_words = [
            "calculate",
            "plus",
            "minus",
            "times",
            "divided by",
            "multiply",
            "subtract",
            "add",
        ]

        return any(
            word in text.lower()
            for word in calculation_words
        )