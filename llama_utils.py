import os
from dotenv import load_dotenv; load_dotenv()
import requests

def query_llama_groq(system, user, model=None):
    api_key = os.getenv("GROQ_API_KEY")
    model = model or os.getenv("LLAMA3_MODEL", "llama3-70b-8192")
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "temperature": 0.1,
        "max_tokens": 1024,
        "top_p": 1.0
    }
    resp = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    try:
        out = resp.json()
        return out["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"LLAMA_GROQ_ERROR: {e}\nRaw: {resp.text}"