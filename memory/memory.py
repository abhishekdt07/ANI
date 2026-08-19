import json
import os


class ANIMemory:
    def __init__(self, memory_file):
        self.memory_file = memory_file
        self.memories = self.load()

    def load(self):
        if not os.path.exists(self.memory_file):
            return []

        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            return []

    def save(self):
        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(
                self.memories,
                file,
                indent=4,
                ensure_ascii=False
            )

    def remember(self, information):
        information = information.strip()

        if not information:
            return False

        self.memories.append(information)
        self.save()

        return True

    def get_all(self):
        return self.memories.copy()

    def get_context(self):
        if not self.memories:
            return ""

        return "\n".join(
            f"- {memory}" for memory in self.memories
        )