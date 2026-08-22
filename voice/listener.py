import speech_recognition as sr


class ANIListener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # Ignore tiny background noise
        self.recognizer.energy_threshold = 300

        # Automatically adjust to the room
        self.recognizer.dynamic_energy_threshold = True

        # Don't wait forever for speech
        self.recognizer.pause_threshold = 0.8

        self.microphone = sr.Microphone()

        print("🎤 ANI microphone initialized.")

        # Calibrate microphone once
        with self.microphone as source:

            print("🎧 Calibrating microphone...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        print("🎤 Microphone ready.")

    def listen(self):

        with self.microphone as source:

            print("\n🎤 Listening...", flush=True)

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:

                # No speech — silently listen again
                return None

        print("🧠 Processing...", flush=True)

        try:

            text = self.recognizer.recognize_google(
                audio
            )

            text = text.strip()

            if text:

                print(
                    f"You said: {text}",
                    flush=True
                )

                return text

            return None

        except sr.UnknownValueError:

            # Couldn't understand speech.
            # Don't make ANI speak every time.
            return None

        except sr.RequestError as e:

            print(
                f"Speech recognition service error: {e}"
            )

            return None


if __name__ == "__main__":

    listener = ANIListener()

    print("\nListener test started.")
    print("Say something, or press Ctrl+C to stop.")

    try:

        while True:

            result = listener.listen()

            if result:

                print(f"Recognized: {result}")

    except KeyboardInterrupt:

        print("\nListener stopped.")