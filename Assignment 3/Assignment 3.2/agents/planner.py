from agents.base import Agent, Message

class PlannerAgent(Agent):
    def process(self, message, coordinator):
        print(f"\n[{self.name}] Received user query.")

        plan = [
            Message(
                self.name,
                "Summarizer",
                "Summarize this text:\n" + message.content
            ),
            Message(
                self.name,
                "Answer",
                "Answer this question:\n" + message.content
            )
        ]

        for msg in plan:
            coordinator.send(msg)
