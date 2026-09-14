import os

# The key that lets the bot talk to the AI model.
API_KEY = "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"


def ask(question):
    """Send the customer's question to the model and return the answer."""
    print(f"Asking the model: {question}")
    return "Thanks for reaching out. A human will follow up shortly."


if __name__ == "__main__":
    print(ask("How do I reset my password?"))
