"""
Summary:
    This module is to deploy the open-source model in local with basic UI (Gradio 5.44.1)
    Combined with audio and image output functionality

Usage:
    Run "python3 _filename_.py" in "tests" directory
    Copy The Localhost URL, run on local browser

Behaviors:
    - Allow user to type in quesiton, and get return from open-source model
    - User can choose which model they want to use
    - User can do the audio input, and return of audio answer
    - User can generate an image

Reference:
    OpenAI API Doc, text generation. (https://platform.openai.com/docs/guides/text)
    Gradio Doc, chatinterface. (https://www.gradio.app/docs/gradio/chatinterface)
"""

# Import
import gradio as gr # For UI
import os # For retrieve private key
from dotenv import load_dotenv
from openai import OpenAI

# Enable to get key with further debug
load_dotenv(override=True) # replace existing one, if os.environ already set
openai_api_key = os.getenv("OPENAI_API_KEY") # Look up the key in process's level

client = OpenAI()
MODEL = "gpt-4o-mini"

system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."

# Based on upgraded Gradio, the "message" is prompt to use, "history" is past conversation 
def chat(message, history):
    messages = (
        [{"role":"system", "content": system_message}] 
        + history 
        + [{"role": "user", "content": message}]
    )
    stream = client.chat.completions.create(
        model = MODEL,
        messages = messages,
    )
    return stream.choices[0].message.content 

# "fn" combined with the response of the chatbot based on the user input and chat history
gr.ChatInterface(fn=chat, type = "messages").launch()

# Use "watchdog" package to auto-reload your python file:
#   watchmedo auto-restart --pattern="*.py" --recursive python test_02.py

