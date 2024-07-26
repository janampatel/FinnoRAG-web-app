from langchain_qdrant import Qdrant
from langchain.embeddings import SentenceTransformerEmbeddings
from qdrant_client import QdrantClient

embeddings = SentenceTransformerEmbeddings(model_name="baconnier/Finance_embedding_large_en-V1.5")

url = "http://localhost:6333"

client = QdrantClient(
    url=url, prefer_grpc=False
)

print(client)
print("##############")

db = Qdrant(client=client, embeddings=embeddings, collection_name="financial_db")

print(db)
print("######")
query = "What is Metastatic disease?"

docs = db.similarity_search_with_score(query=query, k=2)
for i in docs:
    doc, score = i
    print({"score": score, "content": doc.page_content, "metadata": doc.metadata})