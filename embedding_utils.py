import os
from dotenv import load_dotenv; load_dotenv()
from sentence_transformers import SentenceTransformer

EMBED_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
_model = None

def get_embedding_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model

def embed_texts(texts):
    model = get_embedding_model()
    return model.encode(texts, convert_to_tensor=False).tolist()