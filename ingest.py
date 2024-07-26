import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain_qdrant import Qdrant
from transformers import AutoTokenizer, AutoModel
import torch
from sentence_transformers import SentenceTransformer 
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="baconnier/Finance_embedding_large_en-V1.5")


print("**************************")
print(embeddings)
print("**************************")


loader = DirectoryLoader('data/', glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)
# documents = str(documents)
print("**************************")
print(type(documents))
print("**************************")

# texts = text_splitter.create_documents(documents)


print("**************************")
print(type(texts))
print("**************************")


url = "http://localhost:6333" 

qdrant = Qdrant.from_documents(
    texts, 
    embeddings, 
    url=url,
    # prefer_grpc=False,     
    collection_name="financial_db",
)

print("Vector DB Successfully Created!")
