from agents.planner import PlannerAgent
from agents.summarizer import SummarizerAgent
from agents.answer import AnswerAgent
from agents.base import Coordinator, Message

def run_app(user_query):
    coordinator = Coordinator()

    # Create and register agents
    planner = PlannerAgent("Planner")
    summarizer = SummarizerAgent("Summarizer")
    answerer = AnswerAgent("Answer")

    coordinator.register_agent(planner)
    coordinator.register_agent(summarizer)
    coordinator.register_agent(answerer)

    # Send initial message to planner
    initial_message = Message("User", "Planner", user_query)
    coordinator.send(initial_message)
