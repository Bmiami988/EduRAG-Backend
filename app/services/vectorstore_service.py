from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

_vectorstore = None

def init_vectorstore():
    global _vectorstore

    _vectorstore = Chroma(
        persist_directory="edurag_db",
        embedding_function=embedding_model
    )

def get_vectorstore():
    if _vectorstore is None:
        raise Exception("Vector store not initialized")
    return _vectorstore