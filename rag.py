import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./vectordb"
)

collection = client.get_or_create_collection(
    name="company_docs"
)
def retrieve(query):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]
    metadata = results["metadatas"][0]

    return docs, metadata
