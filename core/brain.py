from ollama import chat


class ANIBrain:
    def __init__(self, memory=None):
        self.memory = memory or []

        self.conversation = [
            {
                "role": "system",
                "content": (
                    "Your name is ANI. "
                    "You are Abhi's personal AI assistant. "
                    "Always identify yourself as ANI, never as Qwen. "
                    "Be friendly, helpful, and conversational. "
                    "Use conversation history and saved memory when answering. "
                    "Do not invent memories."
                )
            }
        ]

        self.load_memory()


    def load_memory(self):
        if not self.memory:
            return

        memory_text = "\n".join(
            f"- {item}" for item in self.memory
        )

        self.conversation.append(
            {
                "role": "system",
                "content": (
                    "These are things ANI has saved about Abhi:\n"
                    + memory_text
                )
            }
        )


    def ask(self, user_input):
        self.conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        response = chat(
            model="qwen3:4b",
            messages=self.conversation,
            stream=False
        )

        assistant_response = response["message"]["content"]

        self.conversation.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

        return assistant_response