import faiss
import pickle


class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        self.index.add(embeddings)

    def save(self, index_path, metadata_path, metadata):
        faiss.write_index(self.index, index_path)
        with open(metadata_path, "wb") as f:
            pickle.dump(metadata, f)

    @staticmethod
    def load(index_path, metadata_path):
        index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
            metadata = pickle.load(f)
        return index, metadata

    @staticmethod
    def search(index, query_embedding, metadata, top_k=5):
        distances, indices = index.search(query_embedding, top_k)
        results = [metadata[i] for i in indices[0]]
        return results
    
    @staticmethod
    def search(index, query_embedding, metadata, top_k=5, product_filter=None):
        """
        Performs hybrid retrieval:
        1. Vector similarity search
        2. Optional metadata section filtering
        """

        # Search wider pool first
        distances, indices = index.search(query_embedding, top_k * 3)

        results = []

        for i in indices[0]:
      
            if product_filter:
                if metadata[i]["product"] != product_filter:
                    continue

            results.append(metadata[i]["text"])

            if len(results) == top_k:
                break

        return results

 
