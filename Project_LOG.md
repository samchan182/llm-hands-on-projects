# Q&A

<br>

> [!IMPORTANT]
> Document learnings in a Q&A format.

## Docstrings or Comment?
Comment is for developer<br>
Docstrings is for user of this code/function <br>
Never use __(''')__, it will create unnecessary memory

## Will Python code change by environment?
No! python code does not change the code based on environment. Different environment means the <u>availablility of packages</u> changes.<br>
The only difference is the package installation. 

## Why use .env file to store API key?
A .env file is used to store sensitive information like API keys securely. It should be added to .gitignore so it is not included in version control.

## How to make sure your .env file is being ignored by git?
(base) samchan@chenzisnslaptop llm-hands-on-projects % git check-ignore .env

.env

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

## What is relationship between LLM and machine learning?
Machine learning is a board field of study. In fact, LLM is a specific, advanced type of machine learning model. 

## Why OpenAI has python SDKs?
Almost every major services provides SDKs (AWS OpenAI Stripe...). For each programming language, they has an API to speak to "raw HTTP", the sending web request with specific formats.  

## what is SDKs?
Software Development Kit. To prevent to 'talk' to the system where you need to build everything from scratch. It gives you some pre-existed works from someone else.

## Why we need to setup Anaconda in advance?
Anaconda is a distribution of python, which is bundled with conda package manager, with many pre-installed packages, for ML/data science. An environment is just a simply folder contains many installed packaged. 

When you in (llms) environment, it tells your terminal to <u>use python and package in this particular folder</u>. s

While the (base) is default conda environment. It shows once you install conda. 

## What's pipeline?
A set of data processing elements connected in series. Output of one element is the input of next element. 

It's like assembly line in car factory, start wity body shop, next to plaint shop, etc...

## Why HuggingFace has pipeline?
Using machine learning models (especially transformers) involves multiple complex steps that must happen in the correct order.

Hugging Face pipeline is a great way to use model for inference.You can use simiple API to dedicate serveral tasks. Hugging Face __"pipeline()"__ is like Swiss Army Knife for AI tasks. After authentication, you get access to a huge collection of pre-trained models that handle different tasks with just one line of code

## What is HuggingFace Transformers?
HuggingFace Transformers is a python library that provides pre-trained model, easy-to-use piipelines, training tools, and model architechture. 

Hugging Face is not just a storage platform (like github), it's comprehensive AI/ML platform. When you use transformers library, it will downloads the model to your running maching, and load into your RAM/GPU, and do the inference. 

## Why HuggingFace needs API key for authorization?
Even though this platform is open-source, but it doesn't mean unlimitted access. And some of the model is huge, with ID limit, the download bandwidth (maximum rate of data transfer) costs will the crash of servers. 

## What is the relationship between Tokenizer and Model?
Model and tokenizer are technically separate but functionally inseparable. Tokenizer decides what form of data can put into the neural network. Row data (user input) can be transfer into byte-pair, word piece, sentence piece, etc. 

Usually a "Model" release with three files, 
1. The model weights (the neural network)
2. The tokenizer (how to convert text to numbers)
3. The config files (architecture details)

The model can not function without it own specific tokenizer.

## 