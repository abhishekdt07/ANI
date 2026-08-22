import pyttsx3


class ANISpeaker:
    def __init__(self):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty("voices")

        # ANI's female voice
        self.engine.setProperty("voice", voices[1].id)

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):
        print(f"ANI: {text}")

        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    speaker = ANISpeaker()

    speaker.speak(
        "Hello Abhi. I am ANI. "
        "This is my voice."
    )