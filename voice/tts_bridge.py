import os
import subprocess


# --------------------------------------------------
# AURA PROJECT DIRECTORY
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# --------------------------------------------------
# TTS SERVER
# --------------------------------------------------

SERVER = os.path.join(
    BASE_DIR,
    "voice",
    "tts_server.py"
)


# --------------------------------------------------
# PYTHON USED BY KOKORO
# --------------------------------------------------

TTS_PYTHON = r"C:\AURA-TTS\Scripts\python.exe"


# --------------------------------------------------
# SPEAK
# --------------------------------------------------

def speak(text):

    if not text:
        return

    text = str(text).strip()

    if not text:
        return

    try:

        subprocess.Popen(
            [
                TTS_PYTHON,
                SERVER,
                text
            ],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

    except Exception as e:

        print(
            f"ANI voice error: {e}"
        )