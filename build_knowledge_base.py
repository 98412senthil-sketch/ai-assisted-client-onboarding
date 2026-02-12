from services.knowledge_ingestion.pdf_extractor import extract_pdf_text
from services.knowledge_ingestion.chunker import chunk_text_with_metadata
from services.knowledge_ingestion.embedding_model import EmbeddingModel
from services.knowledge_ingestion.vector_store import VectorStore

print("Extracting PDF...")
text = extract_pdf_text("290423-Booklet-English.pdf")

print("Chunking...")
chunks = chunk_text_with_metadata(text)

print(f"Total chunks: {len(chunks)}")

print("Embedding...")
embedding_model = EmbeddingModel()

# IMPORTANT: Extract text only for embedding
texts = [c["text"] for c in chunks]

embeddings = embedding_model.embed_documents(texts)

print("Building FAISS index...")
vector_store = VectorStore(embeddings.shape[1])
vector_store.add_embeddings(embeddings)

print("Saving index...")
vector_store.save(
    "sbi_vector.index",
    "sbi_chunks.pkl",
    chunks  # <-- enriched metadata saved here
)

print("Knowledge base built successfully.")
