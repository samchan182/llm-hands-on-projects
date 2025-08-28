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

# Client builds a POST request, sends to OpenAI API, handles HTTP calls, with authentication
load_dotenv() # The private key
client = OpenAI()

# The Chat Completions API format
messages = [
    {"role": "user", "content": "What is bond in financial investment?"}
]

# It uses OpenAI python API documentation, stardard format of streaming responses
stream = client.chat.completions.create(
    model = MODEL_GPT,
    messages = messages,
    stream = True # They will sent back chunks of token 
)

for event in stream:
    content = event.choices[0].delta.content
    if content:
        print(content, end='', flush=True)


