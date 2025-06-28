from agents.base import Agent, Message
from openai import OpenAI

client = OpenAI()

class SummarizerAgent(Agent):
    def process(self, message, coordinator):
        text = message.content.replace("Summarize this text:\n", "")
        print(f"\n[{self.name}] Summarizing text...")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful summarizer."},
                {"role": "user", "content": f"Summarize this text:\n\n{text}"}
            ]
        )
        summary = completion.choices[0].message.content.strip()

        coordinator.send(Message(self.name, "Coordinator", summary))
