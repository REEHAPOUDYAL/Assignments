from agents.base import Agent, Message
from openai import OpenAI

client = OpenAI()

class AnswerAgent(Agent):
    def process(self, message, coordinator):
        question = message.content.replace("Answer this question:\n", "")
        print(f"\n[{self.name}] Answering question...")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful expert answering questions."},
                {"role": "user", "content": question}
            ]
        )
        answer = completion.choices[0].message.content.strip()

        coordinator.send(Message(self.name, "Coordinator", answer))
