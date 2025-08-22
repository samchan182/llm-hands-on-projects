"""
HOW TO USE? 
Run "python3 _filename_.py", it returns the answer of pre-settig question by using OpenAI API

This is program to output LLM answer by pre-setting question.
The base model is default GPT-4o-mini.(multiple models to choose)
The asking question is default "What is bond in financial investment?".
"""
# import
from dotenv import load_dotenv # .env in root directory
from openai import OpenAI 

MODEL_GPT = "gpt-4o-mini"

# TASK: use qwen open-source model to produce output
# MDOEL_QWEN = "" # Add to .env file

# OpenAI will verfity once you call 
load_dotenv()
client = OpenAI()

# format 
messages = [
    {"role": "user", "content": "What is bond in financial investment?"}
]

# The respond need to steam word by word for user experience
# It uses OpenAI python API documentation, stardard format of streaming responses
stream = client.chat.completions.create(
    model = MODEL_GPT,
    messages = messages,
    stream = True
) # positional arguments is not allowed

for event in stream:
    content = event.choices[0].delta.content
    if content:
        print(content, end='', flush=True)


