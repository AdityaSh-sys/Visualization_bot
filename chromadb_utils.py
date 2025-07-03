import chromadb
from chromadb.config import Settings

# Use DuckDB instead of SQLite
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db_storage"  # folder for storage
))

def get_chroma_client(collection_name="df_records"):
    # Ensure the collection exists or create it
    col_exists = any(c.name == collection_name for c in client.list_collections())
    if col_exists:
        col = client.get_collection(name=collection_name)
    else:
        col = client.create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})
    return col

def upsert_embeddings(chroma_col, ids, embeddings, metadatas, documents):
    chroma_col.upsert(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents
    )

def query_similar(chroma_col, query_embedding, n_results=7):
    return chroma_col.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
