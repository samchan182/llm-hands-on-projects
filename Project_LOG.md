# Q&A

<br>

> [!IMPORTANT]
> Document learnings in a Q&A format.

## Docstrings or Comment?
Comment is for developer <br>
Docstrings is for user of this code/function <br>
Never use __(''')__, it will create unnecessary memory

## Will Python code change by environment?
No! python code does not change the code based on environment. Different environment means the <u>availablility of packages</u> changes.<br>
The only difference is the package installation. 

## Why use .env file to store API key?
A .env file is used to store sensitive information like API keys securely. It should be added to .gitignore so it is not included in version control.

## Three ways of using models:
1. Chat interface
2. Cloud APIs
3. Direct inference

## What is Ollama doing behind your local?
Ollama is like a coffee machine you buy (download), and you put it into your kitchen (local) to make coffee. 

Ollama Applicaition is like put your coffee machine into active mode (turn on application). Now your local become a server. 

Your python code is like the process / steps of making coffee. To do the specific jobs for you. Ollama is a server running behind, it's the client-server agritecture.

## Why token is so important in LLM?
The model cannot see the word as human being. Each sentence need to convert into series of "TOEKN", and convert into numerical representation, to predict the next "word".

OpenAI provides a "Tokenizer" to understand how tokens is being created by human language. https://platform.openai.com/tokenizer

## What is context window?
It also called context length, the maximun number of tokens a LLM can process at one time. The short-term memory for the entire LLM's conversation. 

Which is including <u>current prompt</u> + <u>current ouput</u> + previous processed <u>history tokens</u>.

## What is API cost?
The price you pay for using this LLM, it is paying for the number of tokens being processed, both input tokens and output tokens. 

# What is relationship between LLM and machine learning?
Machine learning is a board field of study. In fact, LLM is a specific, advanced type of machine learning model. 

# Why OpenAI has python SDKs?
Almost every major services provides SDKs (AWS OpenAI Stripe...). For each programming language, they has an API to speak to "raw HTTP", the sending web request with specific formats.  

# Why we need to set the System prompt?

# what is SDK?
Software Development Kit. To prevent to 'talk' to the system where you need to build everything from scratch. It gives you some pre-existed works from someone else.

# Difference between commit and contribution in github profile?

# Why we need to setup Anaconda in advance?
Anaconda is a distribution of python, which is bundled with conda package manager, with many pre-installed packages, for ML/data science. 
An environment is just a simply folder contains many installed packaged. 

When you in (llms) environment, it tells your terminal to <u>use python and package in this particular folder</u>. 

While the (base) is default conda environment. It shows once you install conda. 
# 


