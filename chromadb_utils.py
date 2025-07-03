import chromadb
from chromadb.config import Settings

# Use DuckDB backend only (no SQLite)
settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=None  # in-memory mode
)
client = chromadb.Client(settings)

def get_chroma_client(collection_name="df_records"):
    names = [c.name for c in client.list_collections()]
    if collection_name in names:
        return client.get_collection(name=collection_name)
    return client.create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})

def upsert_embeddings(chroma_col, ids, embeddings, metadatas, documents):
    chroma_col.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)

def query_similar(chroma_col, query_embedding, n_results=7):
    return chroma_col.query(query_embeddings=[query_embedding], n_results=n_results)
