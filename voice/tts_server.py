import os
import re
import sys

import soundfile as sf
from kokoro import KPipeline


# --------------------------------------------------
# UTF-8 CONSOLE
# --------------------------------------------------

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


# --------------------------------------------------
# ANI NEURAL VOICE SERVER
# --------------------------------------------------

class ANIVoiceServer:

    def __init__(self):

        print("Loading ANI neural voice...")

        self.pipeline = KPipeline(
            lang_code="a",
            repo_id="hexgrad/Kokoro-82M"
        )

        # Natural female Kokoro voice
        self.voice = "af_heart"

        # 1.0 = normal speed
        self.speed = 0.95

        print("ANI voice engine READY.")

    # --------------------------------------------------
    # TEXT CLEANING
    # --------------------------------------------------

    def clean_text(self, text):

        # Better pronunciation for Abhi
        text = re.sub(
            r"\bAbhi\b",
            "Ah-bee",
            text,
            flags=re.IGNORECASE
        )

        # Make ANI sound like a name,
        # NOT "A N I"
        text = re.sub(
            r"\bANI\b",
            "Ani...",
            text,
            flags=re.IGNORECASE
        )

        # Remove emojis/symbols that can cause
        # Windows console problems
        text = text.encode(
            "ascii",
            "ignore"
        ).decode()

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

        if not text or not text.strip():
            return

        text = self.clean_text(text)

        print(f"Speaking: {text}")

        generator = self.pipeline(
            text,
            voice=self.voice,
            speed=self.speed
        )

        audio_file = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "ani_speech.wav"
            )
        )

        for _, _, audio in generator:

            sf.write(
                audio_file,
                audio,
                24000
            )

            print(
                f"Audio saved: {audio_file}"
            )

            # Windows audio playback
            os.startfile(audio_file)

            return


# --------------------------------------------------
# COMMAND LINE ENTRY
# --------------------------------------------------

def main():

    server = ANIVoiceServer()

    # Text supplied from command line
    if len(sys.argv) > 1:

        text = " ".join(sys.argv[1:])

        server.speak(text)

        return


if __name__ == "__main__":
    main()