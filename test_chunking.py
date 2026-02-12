from services.knowledge_ingestion.pdf_extractor import extract_pdf_text
from services.knowledge_ingestion.chunker import chunk_text

text = extract_pdf_text("290423-Booklet-English.pdf")
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")
print("\nSample chunk:\n")
print(chunks[0][:800])
 
