# Following up with the 5-3.py

# Two additioal import
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# The following code is same as 5-3.py til 3D struction

"""4 lines of code section"""

# create a new Chat with OpenAI
llm = ChatOpenAI(temperature=0.7, model_name=MODEL) # chat abstraction

# set up the conversation memory for the chat
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True) 
# return_message: makes it return past messages instead of plain text.

# the retriever is an abstraction over the VectorStore that will be used during RAG
retriever = vectorstore.as_retriever()

# putting it together: set up the conversation chain with the GPT 4o-mini LLM, the vector store and memory
conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
# Wires 3 things (lm, retriever, memory) into RAG pipeline 

"""Abrove 4 line of code is simply instructions using Chain with RAG, and memory"""

"""
Your code builds a conversational RAG system 
→ LLM answers questions, memory keeps context, retriever pulls external knowledge.

User Question
      │
      ▼
 Chat History (Memory) ──►
      │
      ▼
Retriever (Vector DB) ──► [Relevant Chunks]
      │
      ▼
         LLM (ChatOpenAI)
      │
      ▼
    Final Answer
"""

query = "Can you describe Insurellm in a few sentences"
result = conversation_chain.invoke({"question":query})
print(result["answer"])

# It make the user query into vector, and look up in Chrome datastore, find simliaty,
# Sent the output to OpenAI

# set up a new conversation memory for the chat
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

# putting it together: set up the conversation chain with the GPT 4o-mini LLM, the vector store and memory
conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

# bring up with Gradio

# Wrapping in a function - note that history isn't used, as the memory is in the conversation_chain
def chat(message, history):
    result = conversation_chain.invoke({"question": message})
    return result["answer"]

# And in Gradio:
view = gr.ChatInterface(chat, type="messages").launch(inbrowser=True)

