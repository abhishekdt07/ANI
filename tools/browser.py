import webbrowser
from urllib.parse import quote


class ANIBrowser:

    def open_website(self, website):

        websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "linkedin": "https://www.linkedin.com",
            "gmail": "https://mail.google.com",
            "chatgpt": "https://chatgpt.com",
        }

        key = website.lower().strip()

        # -------------------------
        # WHATSAPP DESKTOP
        # -------------------------

        if key == "whatsapp":

            webbrowser.open("whatsapp:")

            return "Opening WhatsApp."

        # -------------------------
        # WEBSITES
        # -------------------------

        if key not in websites:

            return None

        webbrowser.open(
            websites[key]
        )

        return f"Opening {key}."

    # -------------------------
    # GOOGLE SEARCH
    # -------------------------

    def search(self, query):

        query = query.strip()

        if not query:

            return None

        url = (
            "https://www.google.com/search?q="
            + quote(query)
        )

        webbrowser.open(url)

        return (
            f"Searching Google for {query}."
        )