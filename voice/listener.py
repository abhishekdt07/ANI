import speech_recognition as sr


class ANIListener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone(
            device_index=1
        )

        print("🎤 ANI microphone initialized.")

    def listen(self):

        with self.microphone as source:

            print("\n🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=12
                )

            except sr.WaitTimeoutError:

                print("ANI: I didn't hear anything.")
                return None

        try:

            print("🧠 Processing...")

            text = self.recognizer.recognize_google(
                audio
            )

            print(f"You said: {text}")

            return text

        except sr.UnknownValueError:

            print("ANI: I couldn't understand that.")
            return None

        except sr.RequestError as e:

            print(f"ANI: Speech recognition error: {e}")
            return None


if __name__ == "__main__":

    listener = ANIListener()

    while True:

        text = listener.listen()

        if text:

            if text.lower() in ["exit", "quit"]:

                print("ANI: Goodbye, sir.")
                break