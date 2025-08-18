"""
The Purpose: Using OpenAI API to generate the webpage content into markdown and JSON
"""

# import 
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import ollama

# Contants
MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# Set up the environment
load_dotenv()
openai = OpenAI()

# Your question input
question = '''What is bond in financial investment?'''

# prompts
system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"
user_prompt = "Please give a detailed explanation to the following question: " + question

# messages
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# get gpt4o to answer while streaming, also switch to llama
stream = openai.chat.completions.create(model=MODEL_GPT, messages=messages,stream=True)
    
response = ""
display_handle = display(Markdown(""), display_id=True)
for chunk in stream:
    response += chunk.choices[0].delta.content or ''
    response = response.replace("```","").replace("markdown", "")
    update_display(Markdown(response), display_id=display_handle.display_id)


# Get Llama 3.2 to answer
response = ollama.chat(model=MODEL_LLAMA, messages=messages)
reply = response['message']['content']
display(Markdown(reply))
