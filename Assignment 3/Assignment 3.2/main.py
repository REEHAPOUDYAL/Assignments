from app import run_app
import os 


os.environ["OPENAI_API_KEY"] = "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"


if __name__ == "__main__":
    with open("data/article.txt", "r", encoding="utf-8") as f:
        article_text = f.read().strip()

    query = (
        f"{article_text}\n\n"
        "Question: What are the main points of the article, and why is renewable energy important?"
    )

    run_app(query)
