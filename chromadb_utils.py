import chromadb
from chromadb.config import Settings

# ✅ Use DuckDB + Parquet, completely avoiding SQLite
settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=None  # ✅ disables persistence to avoid SQLite dependency
)

# ✅ Create an in-memory Chroma client (safe for Streamlit Cloud)
client = chromadb.Client(settings)

def get_chroma_client(collection_name="df_records"):
    # ✅ Avoid SQLite by using in-memory collection logic
    collections = client.list_collections()
    existing_names = [col.name for col in collections]
    if collection_name in existing_names:
        return client.get_collection(name=collection_name)
    else:
        return client.create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})

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
