import os
import time
import pyautogui


class ANIWhatsApp:

    def open_whatsapp(self):

        print("Opening WhatsApp...")

        os.system("start whatsapp:")

        time.sleep(4)

        return True

    def find_chat(self, contact_name):

        contact_name = contact_name.strip()

        if not contact_name:
            return False

        print(
            f"Searching WhatsApp for: {contact_name}"
        )

        time.sleep(1)

        # Open WhatsApp search
        pyautogui.hotkey(
            "ctrl",
            "f"
        )

        time.sleep(0.5)

        # Clear previous search
        pyautogui.hotkey(
            "ctrl",
            "a"
        )

        pyautogui.write(
            contact_name,
            interval=0.05
        )

        time.sleep(2)

        # Select the first search result.
        #
        # NOTE:
        # We will improve this later so ANI verifies
        # the exact contact instead of blindly choosing
        # the first result.

        pyautogui.press(
            "down"
        )

        time.sleep(0.5)

        pyautogui.press(
            "enter"
        )

        time.sleep(1)

        print(
            f"WhatsApp chat opened: {contact_name}"
        )

        return True