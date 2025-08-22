"""
This is a programm with user interface, with usage of different model.
You are also use audio and image output functionaliy.
"""

# This should include a Gradio UI, streaming, use of the system prompt to add expertise, and the ability to switch between models. 
# 
# Bonus points if you can demonstrate use of a tool!
# 
# If you feel bold, see if you can add audio input so you can talk to it, and have it respond with audio.



# Some packages doesn't exist in python3.13 on Apple Silicon, or Change conda environment
import gradio as gr 

# Logic
def greet(name):
    return "Hello " + name + "!"

# Example code from Gradio Doc
demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch()
