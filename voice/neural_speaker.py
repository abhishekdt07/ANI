import os
import re
import sys

from kokoro import KPipeline
import soundfile as sf


# --------------------------------------------------
# WINDOWS UTF-8 SUPPORT
# --------------------------------------------------

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


class ANINeuralSpeaker:

    def __init__(self):

        print("Loading ANI neural voice...")

        self.pipeline = KPipeline(
            lang_code="a",
            repo_id="hexgrad/Kokoro-82M"
        )

        # Natural female voice
        self.voice = "af_heart"

        # Keep current natural speed
        self.speed = 1.0

        print("ANI neural voice loaded.")

    # --------------------------------------------------
    # CLEAN TEXT BEFORE SPEECH
    # --------------------------------------------------

    def clean_text(self, text):

        # Convert ANI's name to a pronunciation Kokoro handles better
        text = re.sub(
            r"\bAbhi\b",
            "Ah-bee",
            text,
            flags=re.IGNORECASE
        )

        # Remove emojis and unusual Unicode symbols
        text = text.encode(
            "ascii",
            "ignore"
        ).decode()

        # Add a small pause after "I am"
        text = re.sub(
            r"\bI am ANI\b",
            "I am... ANI",
            text,
            flags=re.IGNORECASE
        )

        # Clean extra spaces
        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        return text

    # --------------------------------------------------
    # SPEAK
    # --------------------------------------------------

    def speak(self, text):

        print(f"ANI: {text}")

        clean_text = self.clean_text(text)

        generator = self.pipeline(
            clean_text,
            voice=self.voice,
            speed=self.speed
        )

        audio_file = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "ani_speech.wav"
            )
        )

        generated = False

        for _, _, audio in generator:

            sf.write(
                audio_file,
                audio,
                24000
            )

            generated = True
            break

        if not generated:

            print("ANI: No audio was generated.")

            return False

        print(
            f"Audio saved to: {audio_file}"
        )

        try:

            os.startfile(audio_file)

        except Exception as error:

            print(
                f"Could not automatically play audio: {error}"
            )

        return True


# --------------------------------------------------
# DIRECT TEST / TTS BRIDGE
# --------------------------------------------------

if __name__ == "__main__":

    speaker = ANINeuralSpeaker()

    if len(sys.argv) > 1:

        text = " ".join(
            sys.argv[1:]
        )

        speaker.speak(text)

    else:

        speaker.speak(
            "Hello Ah-bee. "
            "I am... ANI. "
            "My natural voice is now online."
        )