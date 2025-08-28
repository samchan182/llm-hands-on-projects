"""
Summary:
    This module is to deploy the open-source model in local with basic UI
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
    https://qwen.readthedocs.io/en/latest/getting_started/quickstart.html 
    https://www.gradio.app/guides/quickstart
    https://www.gradio.app/guides/creating-a-chatbot-fast
"""

# Some packages doesn't exist in python3.13 on Apple Silicon, or Change conda environment
import gradio as gr # Use "pip show grdaio" to check installation

# Interface Logic
def greet(name, intensity):
    return "This is the successfully demo, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)



# A simple UI allow boarder degree of freedom:
#   demo.launch()
#
# Use "watchdog" package to auto-reload your python file:
#   watchmedo auto-restart --pattern="*.py" --recursive python test_02.py


# A default chatbox UI
gr.load_chat("http://localhost:11434/v1/", model="llama3.2", token="***").launch()
