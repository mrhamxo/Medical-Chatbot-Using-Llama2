from flask import Flask, render_template, jsonify, request

import pinecone
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

#from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

from src.helper import download_hugging_face_embedding_model
from src.prompt import *

from dotenv import load_dotenv
import os

import tensorflow as tf
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

embeddings = download_hugging_face_embedding_model()

# Initialize Pinecone client
pinecone = Pinecone(
    api_key = PINECONE_API_KEY,
    serverless = ServerlessSpec(
        cloud = 'aws',
        region = 'us-east-1'
    )
)

# Specify your index
index_name = "medical-chatbot"

# Initialize the embedding model
#embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


doc_search = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)


PROMPT = PromptTemplate(
    template = prompt_template, 
    input_variables = ["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(
        model = "model/llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type = "llama",
        config = {
                 'max_new_tokens' : 512,
                 'temperature' : 0.8
                }
        )

qa = RetrievalQA.from_chain_type(
    llm = llm, 
    chain_type = "stuff", 
    retriever = doc_search.as_retriever(
        search_kwargs = {'k': 2}
    ),
    return_source_documents = True, 
    chain_type_kwargs = chain_type_kwargs
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods = ["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa.invoke({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])


if __name__ == '__main__':
    app.run(debug = True)
