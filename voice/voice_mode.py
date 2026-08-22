import sys

from voice.listener import ANIListener
from voice.tts_bridge import speak
from core.brain import ANIBrain
from core.router import ANIRouter
from memory.memory import ANIMemory
from tools.calculator import try_calculate


class ANIVoiceMode:

    def __init__(self):

        print("\n================================")
        print("        ANI VOICE MODE")
        print("================================")

        self.listener = ANIListener()

        self.memory = ANIMemory("memory.json")

        self.brain = ANIBrain(
            self.memory.get_all()
        )

        self.router = ANIRouter(
            self.memory,
            self.brain
        )

        print("ANI voice mode is ready.")
        speak("Hello Ah-bee. I am ANI. Voice mode is ready.")

    def say(self, text):

        print(f"ANI: {text}")

        try:
            speak(text)
        except Exception as e:
            print(f"Voice error: {e}")

    def run(self):

        while True:

            user_input = self.listener.listen()

            if not user_input:
                continue

            user_input = user_input.strip()

            print(f"You: {user_input}")

            if user_input.lower() in [
                "exit",
                "quit",
                "goodbye"
            ]:

                self.say("Goodbye, sir.")
                break

            route = self.router.route(user_input)

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

                self.router.brain = self.brain

                continue

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

                    continue

            # -------------------------
            # AI BRAIN
            # -------------------------

            if route == "brain":

                response = self.brain.ask(
                    user_input
                )

                self.say(response)

                continue

            # -------------------------
            # FALLBACK
            # -------------------------

            self.say(
                "I'm not sure how to handle that yet."
            )


if __name__ == "__main__":

    try:

        assistant = ANIVoiceMode()

        assistant.run()

    except KeyboardInterrupt:

        print("\nANI stopped.")

    except Exception as e:

        print(f"\nANI error: {e}")