# imports

import os
import requests
from bs4 import BeautifulSoup
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
import anthropic

import gradio as gr # oh yeah!

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")


# Connect to OpenAI, Anthropic and Google; comment out the Claude or Google lines if you're not using them
openai = OpenAI()
claude = anthropic.Anthropic()
google.generativeai.configure()

# A generic system message - no more snarky adversarial AIs!
system_message = "You are a helpful assistant"

# Let's wrap a call to GPT-4o-mini in a simple function
def message_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    completion = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
    )
    return completion.choices[0].message.content

# This can reveal the "training cut off", or the most recent date in the training data
message_gpt("What is today's date?")

# here's a simple function
def shout(text):
    print(f"Shout has been called with input {text}")
    return text.upper()

shout("hello")

# The simplicty of gradio. This might appear in "light mode" - I'll show you how to make this in dark mode later.
# gr.Interface(fn=shout, inputs="textbox", outputs="textbox").launch()

# Adding share=True means that it can be accessed publically
# A more permanent hosting is available using a platform called Spaces from HuggingFace, which we will touch on next week
# NOTE: Some Anti-virus software and Corporate Firewalls might not like you using share=True. If you're at work on on a work network, I suggest skip this test.
# gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True)

# Adding inbrowser=True opens up a new browser window automatically
gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True)