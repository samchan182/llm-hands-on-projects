"""
Prerequisite: Install the "openai" module.
This project uses Ollama as a server to send requests to the model.
Model used: deepseek-r1:1.5b
"""
import openai
import subprocess

def get_ollama_client():
    """Configures and returns a client to connect to the local Ollama server."""
    client = openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
    return client

def ask_model(client, model, question):
    """Sends a question to the specified model and returns the response content."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content

# This block runs only when you execute the file directly
if __name__ == "__main__":
    MODEL_NAME = "deepseek-r1:1.5b"
    QUESTION = "Please give definitions of some core concepts behind LLMs: a neural network"

    # Preparatory step: Pull the model
    print(f"Pulling model '{MODEL_NAME}'. This may take a moment...")
    subprocess.run(["ollama", "pull", MODEL_NAME], capture_output=True, text=True)
    print("Model is ready.")

    # Main logic
    try:
        ollama_client = get_ollama_client()
        print("\nSending request to the model...")
        answer = ask_model(ollama_client, MODEL_NAME, QUESTION)

        print("\n--- Model's Response ---")
        print(answer)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure the Ollama server is running.")