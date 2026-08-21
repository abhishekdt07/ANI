import sounddevice as sd
import speech_recognition as sr


class ANIVoice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.sample_rate = 16000
        self.channels = 1

    def listen(self):
        print("\n🎤 ANI is listening...")

        try:
            audio_data = sd.rec(
                int(10 * self.sample_rate),
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype="int16",
                device=5
            )

            sd.wait()

        except Exception as error:
            print(f"ANI: Microphone error: {error}")
            return None

        print("🧠 ANI is processing...")

        audio = sr.AudioData(
            audio_data.tobytes(),
            self.sample_rate,
            2
        )

        try:
            text = self.recognizer.recognize_google(audio)

            print(f"You said: {text}")

            return text

        except sr.UnknownValueError:
            print("ANI: Sorry, I couldn't understand you.")
            return None

        except sr.RequestError as error:
            print(f"ANI: Speech service error: {error}")
            return None


if __name__ == "__main__":
    voice = ANIVoice()

    text = voice.listen()

    if text:
        print(f"Recognized: {text}")