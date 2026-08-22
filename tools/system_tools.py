import subprocess
import os


class ANISystemTools:

    def open_app(self, app_name):

        app = app_name.lower().strip()

        apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "calc": "calc.exe",
            "chrome": "chrome.exe",
            "edge": "msedge.exe",
            "vscode": "code",
            "vs code": "code",
        }

        if app == "whatsapp":

            os.system("start whatsapp:")

            return "Opening WhatsApp."

        if app not in apps:

            return None

        try:

            subprocess.Popen(
                apps[app],
                shell=True
            )

            return f"Opening {app_name}."

        except Exception as e:

            print(f"System tool error: {e}")

            return None