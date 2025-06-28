# Multi-Agent Conversational QA System
This repository contains my implementation of a simple Multi-Agent Conversational Question Answering (QA) System. The project demonstrates how Large Language Models (LLMs) can collaborate to solve complex tasks by dividing them into subtasks, with each subtask handled by a specialized agent. Communication between these agents is managed through a message-passing mechanism.

# Project Overview
The goal of this project is to process a given text (e.g., an article) and answer a specific question about it by orchestrating a team of AI agents. Each agent has a distinct role, ensuring efficient and structured processing of information. This system highlights the power of modularity and inter-agent communication in building robust LLM applications.

# Key Concepts & My Implementation
Multi-Agent System: I designed a system where multiple independent LLM-powered agents work together to achieve a common goal (answering a question). This approach breaks down complex problems into manageable sub-problems, allowing for more focused and efficient processing.

Specialized Agents: Each agent is given a specific responsibility, making the system modular and scalable:

Planner Agent (PlannerAgent): This agent is the initial point of contact. It receives the user's query and the raw article text. Its primary role is to understand the overall request and strategize how the task should be approached by the other agents. It might break down the query or determine the flow of information.

Summarizer Agent (SummarizerAgent): This agent's job is to process the article content. Guided by the planner's strategy, it extracts key information or generates concise summaries that are directly relevant to the user's question. This helps in distilling large amounts of text into actionable insights.

Answer Agent (AnswerAgent): The final agent in the pipeline. It takes the summarized information (from the Summarizer) and the original question, then synthesizes a coherent and accurate final answer for the user.

Message Passing Communication: I implemented a custom Coordinator and Message class (agents/base.py) to facilitate communication. This system ensures that agents can send structured messages to each other, passing on their outputs or requesting information. This explicit communication flow is crucial for agents to collaborate effectively and ensures that information moves correctly through the pipeline (from planning to summarizing to answering) without a single, monolithic LLM trying to handle everything.

LLM Integration: Each specialized agent leverages a Large Language Model (LLM) to perform its task. In this project, I used the OpenAI API to power these agents, making them intelligent and capable of understanding, processing, and generating human-like text based on their assigned roles.
