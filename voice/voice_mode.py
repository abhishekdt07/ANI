from core.brain import ANIBrain
from core.router import ANIRouter
from memory.memory import ANIMemory

from tools.calculator import try_calculate
from tools.browser import ANIBrowser
from tools.system_tools import ANISystemTools
from tools.whatsapp import ANIWhatsApp

from voice.listener import ANIListener
from voice.tts_bridge import speak


class ANIVoiceMode:

    def __init__(self):

        print("\n================================")
        print("        ANI VOICE MODE")
        print("================================")

        # -------------------------
        # MICROPHONE
        # -------------------------

        self.listener = ANIListener()

        # -------------------------
        # MEMORY
        # -------------------------

        self.memory = ANIMemory(
            "memory.json"
        )

        # -------------------------
        # BRAIN
        # -------------------------

        self.brain = ANIBrain(
            self.memory.get_all()
        )

        # -------------------------
        # ROUTER
        # -------------------------

        self.router = ANIRouter(
            self.memory,
            self.brain
        )

        # -------------------------
        # TOOLS
        # -------------------------

        self.browser = ANIBrowser()

        self.system = ANISystemTools()

        self.whatsapp = ANIWhatsApp()

        print(
            "ANI voice mode is ready."
        )

        self.say(
            "Hello Ah-bee. I am ANI. Voice mode is ready."
        )

    # ==================================================
    # SPEAK
    # ==================================================

    def say(self, text):

        print(
            f"ANI: {text}"
        )

        try:

            speak(text)

        except Exception as e:

            print(
                f"Voice error: {e}"
            )

    # ==================================================
    # WHATSAPP COMMAND
    # ==================================================

    def handle_whatsapp_command(
        self,
        user_input
    ):

        text = user_input.lower()

        # ----------------------------------
        # FIND
        # ----------------------------------

        if "find " in text:

            contact = text.split(
                "find ",
                1
            )[1]

        # ----------------------------------
        # SEARCH
        # ----------------------------------

        elif "search " in text:

            contact = text.split(
                "search ",
                1
            )[1]

        # ----------------------------------
        # CHAT
        # ----------------------------------

        elif "chat with " in text:

            contact = text.split(
                "chat with ",
                1
            )[1]

        else:

            self.say(
                "Tell me the WhatsApp contact you want me to find."
            )

            return True

        # ----------------------------------
        # CLEAN CONTACT NAME
        # ----------------------------------

        contact = contact.replace(
            " on whatsapp",
            ""
        )

        contact = contact.replace(
            " in whatsapp",
            ""
        )

        contact = contact.replace(
            " whatsapp",
            ""
        )

        contact = contact.strip()

        if not contact:

            self.say(
                "I didn't catch the contact name."
            )

            return True

        # ----------------------------------
        # SEARCH
        # ----------------------------------

        self.say(
            f"Searching WhatsApp for {contact}."
        )

        try:

            opened = (
                self.whatsapp.open_whatsapp()
            )

            if not opened:

                self.say(
                    "I couldn't open WhatsApp."
                )

                return True

            found = (
                self.whatsapp.find_chat(
                    contact
                )
            )

            if found:

                self.say(
                    f"I opened the WhatsApp chat for {contact}."
                )

            else:

                self.say(
                    f"I couldn't find {contact} on WhatsApp."
                )

        except Exception as e:

            print(
                f"WhatsApp error: {e}"
            )

            self.say(
                "Something went wrong while opening WhatsApp."
            )

        return True

    # ==================================================
    # SYSTEM COMMAND
    # ==================================================

    def handle_system_command(
        self,
        user_input
    ):

        text = user_input.lower()

        apps = [
            "visual studio code",
            "vscode",
            "vs code",
            "notepad",
            "calculator",
            "calc",
            "chrome",
            "edge",
            "whatsapp",
        ]

        actions = [
            "open",
            "launch",
            "start",
            "run",
        ]

        for app in apps:

            for action in actions:

                if (
                    f"{action} {app}" in text
                    or
                    f"{action} my {app}" in text
                    or
                    f"{action} the {app}" in text
                ):

                    response = (
                        self.system.open_app(
                            app
                        )
                    )

                    if response:

                        self.say(
                            response
                        )

                    else:

                        self.say(
                            f"I couldn't open {app}."
                        )

                    return True

        return False

    # ==================================================
    # BROWSER COMMAND
    # ==================================================

    def handle_browser_command(
        self,
        user_input
    ):

        text = user_input.lower()

        websites = {

            "google":
                "https://www.google.com",

            "youtube":
                "https://www.youtube.com",

            "github":
                "https://github.com",

            "linkedin":
                "https://www.linkedin.com",

            "gmail":
                "https://mail.google.com",

            "chatgpt":
                "https://chatgpt.com",
        }

        for name, url in websites.items():

            if (
                f"open {name}" in text
                or
                f"open my {name}" in text
                or
                f"open the {name}" in text
            ):

                try:

                    self.browser.open_url(
                        url
                    )

                    self.say(
                        f"Opening {name}."
                    )

                except Exception as e:

                    print(
                        f"Browser error: {e}"
                    )

                    self.say(
                        f"I couldn't open {name}."
                    )

                return True

        return False

    # ==================================================
    # PROCESS COMMAND
    # ==================================================

    def process_command(
        self,
        user_input
    ):

        route = self.router.route(
            user_input
        )

        # -------------------------
        # MEMORY
        # -------------------------

        if route == "memory_saved":

            self.say(
                "Got it, sir. I'll remember that."
            )

            self.brain = ANIBrain(
                self.memory.get_all()
            )

            self.router.brain = (
                self.brain
            )

            return

        # -------------------------
        # WHATSAPP
        # -------------------------

        if route == "whatsapp":

            self.handle_whatsapp_command(
                user_input
            )

            return

        # -------------------------
        # SYSTEM
        # -------------------------

        if route == "system":

            self.handle_system_command(
                user_input
            )

            return

        # -------------------------
        # BROWSER
        # -------------------------

        if route == "browser":

            self.handle_browser_command(
                user_input
            )

            return

        # -------------------------
        # CALCULATOR
        # -------------------------

        if route == "calculator":

            result = try_calculate(
                user_input
            )

            if result is not None:

                self.say(
                    f"The answer is {result}."
                )

                return

        # -------------------------
        # AI BRAIN
        # -------------------------

        if route == "brain":

            response = self.brain.ask(
                user_input
            )

            self.say(
                response
            )

            return

        # -------------------------
        # FALLBACK
        # -------------------------

        self.say(
            "I'm not sure how to handle that yet."
        )

    # ==================================================
    # MAIN LOOP
    # ==================================================

    def run(self):

        while True:

            try:

                user_input = (
                    self.listener.listen()
                )

            except KeyboardInterrupt:

                print(
                    "\nANI stopped."
                )

                break

            except Exception as e:

                print(
                    f"Listener error: {e}"
                )

                continue

            if not user_input:

                continue

            user_input = (
                user_input.strip()
            )

            if not user_input:

                continue

            print(
                f"You: {user_input}"
            )

            # -------------------------
            # EXIT
            # -------------------------

            if user_input.lower() in [
                "exit",
                "quit",
                "goodbye",
            ]:

                self.say(
                    "Goodbye, sir."
                )

                break

            # -------------------------
            # PROCESS
            # -------------------------

            try:

                self.process_command(
                    user_input
                )

            except Exception as e:

                print(
                    f"Command error: {e}"
                )

                self.say(
                    "I encountered an error processing that command."
                )


# ======================================================
# START ANI
# ======================================================

if __name__ == "__main__":

    try:

        assistant = ANIVoiceMode()

        assistant.run()

    except KeyboardInterrupt:

        print(
            "\nANI stopped."
        )

    except Exception as e:

        print(
            f"\nANI error: {e}"
        )