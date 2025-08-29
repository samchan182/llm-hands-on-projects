"""
Summary:
    A module to demonstrate calling OpenAI's Chat Completions API

Usage:
    Run "python3 _filename_.py" in "tests" directory

Behavior:
    -It returns the answer of pre-settig question
    -The base model is default GPT-4o-mini.(multiple models to choose)
    -The asking question is default "What is bond in financial investment?".

Reference:
    https://github.com/openai/openai-python 
"""
# import
from dotenv import load_dotenv # .env in root directory
from openai import OpenAI # OpenAI publish python package on PyPl, can install by "pip"

MODEL_GPT = "gpt-4o-mini"

# The private key
load_dotenv() 

# Client builds a POST request, sends to OpenAI API, handles HTTP calls, with authentication
# The Python wrapper for POST request, to OpenAI server HTTP endpoints https://api.openai.com/v1/....
client = OpenAI()

# The Chat Completions API format, Python lists of dictionaries
messages = [
    {"role": "user", "content": "What is bond in financial investment?"}
]

# OpenAI REST API library with steam content
stream = client.chat.completions.create(
    model = MODEL_GPT,
    messages = messages,
    stream = True # They will sent back chunks of token 
    # The API does Server-Sent Events (SSE) over HTTP, not return big JSON, instead of delta ojbects
)

for event in stream:
    content = event.choices[0].delta.content # From "steam = True", the incremental delta object
    if content:
        print(content, end='', flush=True) # End (next line) & Flush means content appear live




