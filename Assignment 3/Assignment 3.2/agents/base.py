class Message:
    """Message container for communication."""
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content


class Agent:
    """Base class for all agents."""
    def __init__(self, name):
        self.name = name

    def process(self, message, coordinator):
        raise NotImplementedError


class Coordinator:
    """Manages communication between agents."""
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        self.agents[agent.name] = agent

    def send(self, message):
        if message.recipient == "Coordinator":
            print(f"\n[Coordinator] Received from {message.sender}:")
            print(message.content)
        else:
            agent = self.agents.get(message.recipient)
            if agent:
                agent.process(message, self)
            else:
                print(f"[Coordinator] Unknown recipient: {message.recipient}")
