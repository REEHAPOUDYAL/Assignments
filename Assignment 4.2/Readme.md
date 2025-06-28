# LLM Prompting Techniques for Sentiment Analysis
This repository contains my project focused on exploring and comparing various prompting techniques for Large Language Models (LLMs), specifically applied to a sentiment analysis task. I implemented and tested Basic, Few-Shot, and Chain-of-Thought (CoT) Prompting strategies to observe their impact on the quality and reasoning of sentiment predictions using a local Transformer model.

# Project Overview
The main objective of this project was to gain a practical understanding of prompt engineering by demonstrating how different ways of instructing an LLM can influence its output for a text classification task. I used the IMDb movie review dataset to classify sentiment (positive or negative) and analyzed how each prompting technique affected the model's ability to provide accurate and insightful sentiment analyses.

# Key Concepts & My Implementation
Pre-trained Transformer Model (GPT-Neo-125M): I utilized EleutherAI/gpt-neo-125M, a relatively small yet capable pre-trained Transformer model from Hugging Face's transformers library, as the core of my sentiment analysis system. This allowed me to run experiments locally (or in a Colab environment) without requiring extensive computational resources.

Prompt Engineering: The central theme of this project was crafting and comparing different prompts to guide the LLM's behavior:

Basic Prompting: This is the most straightforward approach, providing a direct instruction to classify the sentiment of a given review (e.g., "What is the sentiment of the following review? Answer with ONE word only: Positive, Neutral, or Negative.").

Few-Shot Prompting: I implemented this by providing the LLM with a few examples of reviews paired with their correct sentiment labels (Positive, Neutral, Negative) before presenting the review to be analyzed. This helps the model understand the desired format and style of response.

Chain-of-Thought (CoT) Prompting: This advanced technique encourages the LLM to "think step-by-step" before arriving at a final answer. For sentiment analysis, my CoT prompt explicitly instructed the model to:

Identify key emotional phrases.

Classify each phrase's sentiment.

Weigh the overall tone.

Conclude with a single sentiment word.
This aims to elicit more transparent and reasoned outputs.

Sentiment Analysis: I applied these prompting techniques to classify movie reviews from the IMDb dataset into "positive" or "negative" sentiments.

Text Preprocessing: I included a clean_text function to remove HTML tags (<br />) from the raw review text, ensuring cleaner input for the LLM.

Hugging Face Transformers Library: I leveraged this library for easy loading of the pre-trained GPT-Neo model and its tokenizer, as well as for generating text based on the crafted prompts.

Pandas for Data Handling: I used the pandas library to load and inspect the IMDb dataset (IMDB Dataset) to extract sample reviews for analysis.

# Analysis & Observations
After running the notebook and observing the outputs for various movie reviews, I made the following key observations regarding the different prompting techniques:

Basic Prompting:

Often provided a single-word sentiment (Positive, Negative, or Neutral).

While quick, it offered no insight into why the model arrived at that sentiment.

Sometimes struggled with nuanced reviews or those containing both positive and negative elements, leading to potentially less accurate classifications or incomplete responses (as seen in some outputs where the model continued generating beyond the sentiment word).

Few-Shot Prompting:

Significantly improved the adherence to the desired output format (a single sentiment word).

By providing examples, the model better understood the task's scope and the expected response style.

For the example reviews, it often provided a more consistent and arguably more accurate sentiment classification compared to basic prompting, as it had learned from the provided patterns. However, for complex reviews, it could still misinterpret the overall tone (e.g., classifying a review with mixed but ultimately positive sentiment as "Neutral").

Chain-of-Thought (CoT) Prompting:

This technique proved to be the most insightful for understanding the model's reasoning.

The model explicitly broke down the sentiment analysis into logical steps: identifying key phrases, classifying their individual sentiments, and then weighing the overall tone.

While the final sentiment might sometimes align with the other methods, the CoT output provided a transparent and verifiable thought process. This is invaluable for debugging, building trust, and understanding the nuances of the model's interpretation, especially for reviews that are not straightforward.

However, for the GPT-Neo-125M model, the CoT outputs sometimes generated additional, irrelevant text after the structured answer, indicating that even with CoT, smaller models might struggle with strict adherence to complex instructions or maintaining focus over longer generations.

Overall, my experiments demonstrated that Chain-of-Thought prompting, despite its increased token usage, offers the most transparent and often a more robust approach to complex text analysis tasks by guiding the LLM's reasoning. Few-Shot prompting is excellent for enforcing output formats and improving consistency, while basic prompting is suitable for quick, simple classifications where reasoning is n
