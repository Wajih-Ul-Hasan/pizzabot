from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from pathlib import Path
from typing import List

class VectorDB:
    def __init__(self, persist_dir: str):
        Path(persist_dir).mkdir(parents=True, exist_ok=True)
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.db = Chroma(collection_name="pizzabot", embedding_function=self.embeddings, persist_directory=persist_dir)

    def add_texts(self, ids: List[str], texts: List[str]):
        self.db.add_texts(texts=texts, metadatas=[{"id": i} for i in ids], ids=ids)
        self.db.persist()

    def search(self, query: str, k: int = 4):
        return self.db.similarity_search(query, k=k)

vectordb: VectorDB | None = None

def get_vectordb(dir: str) -> VectorDB:
    global vectordb
    if vectordb is None:
        vectordb = VectorDB(dir)
    return vectordb