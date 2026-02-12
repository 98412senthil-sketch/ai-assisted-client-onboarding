from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        embeddings = self.model.encode(documents)
        return np.array(embeddings).astype("float32")

    def embed_query(self, query):
        embedding = self.model.encode([query])
        return np.array(embedding).astype("float32")
 
