import chromadb
from chromadb.config import Settings

# ✅ Explicitly force DuckDB+Parquet and AVOID SQLite completely
settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db_storage",  # or None if no persistence is needed
)

# ✅ Create client using only DuckDB backend
client = chromadb.Client(settings)

def get_chroma_client(collection_name="df_records"):
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
