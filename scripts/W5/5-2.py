
# imports
import os
import glob
from dotenv import load_dotenv
import gradio as gr

# imports for langchain
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter

# price is a factor for our company, so we're going to use a low cost model
MODEL = "gpt-4o-mini"
db_name = "vector_db"

# Load environment variables in a file called .env
load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')

# Read in documents using LangChain's loaders
# Take everything in all the sub-folders of our knowledgebase
# Thank you Mark D. and Zoya H. for fixing a bug here..

folders = glob.glob("knowledge-base/*")

# With thanks to CG and Jon R, students on the course, for this fix needed for some users 
text_loader_kwargs = {'encoding': 'utf-8'}
# If that doesn't work, some Windows users might need to uncomment the next line instead
# text_loader_kwargs={'autodetect_encoding': True}

documents = []
for folder in folders:
    doc_type = os.path.basename(folder) # Get the type of document (company, contract, ..)
    loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    folder_docs = loader.load()
    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type # All put into the metadata
        documents.append(doc)

len(documents) # Shows how many types of documents
documents(24) # Check the document in metadata

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # Data chunk overlap
chunks = text_splitter.split_documents(documents)

len(chunks) # How many chunks it has
chunks[6]

doc_types = set(chunk.metadata['doc_type'] for chunk in chunks)
print(f"Document types found: {', '.join(doc_types)}")

for chunk in chunks:
    if 'CEO' in chunk.page_content: # To check the doc type contains CEO
        print(chunk)
        print("_________")

