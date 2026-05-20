import os
import chromadb

from utils.loader import load_pdf
from utils.chunker import chunk_text
from utils.embeddings import get_embeddings

client = chromadb.PersistentClient(
    path="./vectordb"
)

collection = client.get_or_create_collection(
    name="company_docs"
)

for file in os.listdir("docs"):

    path = f"docs/{file}"

    text = load_pdf(path)

    chunks = chunk_text(text)

    embeddings = get_embeddings(
        chunks
    )

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[f"{file}_{i}"],
            documents=[chunk],
            embeddings=[
                embeddings[i].tolist()
            ],
            metadatas=[
                {
                    "source": file
                }
            ]
        )

print("Documents processed successfully")