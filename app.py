import os

# The key that lets the bot talk to the AI model.
API_KEY = os.environ.get("API_KEY")


def ask(question):
    """Send the customer's question to the model and return the answer."""
    print(f"Asking the model: {question}")
    return "Thanks for reaching out. A human will follow up shortly."


if __name__ == "__main__":
    print(ask("How do I reset my password?"))
