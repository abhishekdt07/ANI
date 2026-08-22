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

                self.memory.remember(
                    information
                )

                return "memory_saved"

        # -------------------------
        # WHATSAPP
        # -------------------------

        if self.is_whatsapp_command(
            lower_text
        ):

            return "whatsapp"

        # -------------------------
        # SYSTEM
        # -------------------------

        if self.is_system_command(
            lower_text
        ):

            return "system"

        # -------------------------
        # BROWSER
        # -------------------------

        if self.is_browser_command(
            lower_text
        ):

            return "browser"

        # -------------------------
        # CALCULATOR
        # -------------------------

        if self.is_calculation(
            text
        ):

            return "calculator"

        # -------------------------
        # AI BRAIN
        # -------------------------

        return "brain"

    # ==================================================
    # WHATSAPP COMMANDS
    # ==================================================

    def is_whatsapp_command(self, text):

        whatsapp_words = [
            "whatsapp",
            "what's app",
            "whats app",
        ]

        action_words = [
            "find",
            "search",
            "chat",
            "message",
            "text",
        ]

        has_whatsapp = any(
            word in text
            for word in whatsapp_words
        )

        has_action = any(
            word in text
            for word in action_words
        )

        return (
            has_whatsapp
            and
            has_action
        )

    # ==================================================
    # SYSTEM COMMANDS
    # ==================================================

    def is_system_command(self, text):

        actions = [
            "open",
            "launch",
            "start",
            "run",
        ]

        apps = [
            "notepad",
            "calculator",
            "calc",
            "chrome",
            "edge",
            "vscode",
            "vs code",
            "visual studio code",
            "whatsapp",
        ]

        has_action = any(
            action in text
            for action in actions
        )

        has_app = any(
            app in text
            for app in apps
        )

        return (
            has_action
            and
            has_app
        )

    # ==================================================
    # BROWSER COMMANDS
    # ==================================================

    def is_browser_command(self, text):

        browser_names = [
            "google",
            "youtube",
            "github",
            "linkedin",
            "gmail",
            "chatgpt",
        ]

        browser_actions = [
            "open",
            "launch",
            "start",
        ]

        has_action = any(
            action in text
            for action in browser_actions
        )

        has_browser = any(
            name in text
            for name in browser_names
        )

        return (
            has_action
            and
            has_browser
        )

    # ==================================================
    # CALCULATOR
    # ==================================================

    def is_calculation(self, text):

        operators = [
            "+",
            "-",
            "*",
            "/",
        ]

        if any(
            operator in text
            for operator in operators
        ):

            return True

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