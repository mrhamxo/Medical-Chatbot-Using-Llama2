from src.helper import load_pdf, text_split, download_hugging_face_embedding_model
import pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

print(PINECONE_API_KEY)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
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

# Creating Embeddings for Each of The Text Chunks & storing
doc_search = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks], 
    embeddings, 
    index_name = index_name
)
