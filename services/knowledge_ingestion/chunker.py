from langchain_text_splitters import RecursiveCharacterTextSplitter



def chunk_text(text, chunk_size=600, chunk_overlap=150):
    """
    Splits document into semantically meaningful chunks.
    Designed for policy and product documents.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = splitter.split_text(text)

    return chunks
 
def chunk_text_with_metadata(text, chunk_size=600, chunk_overlap=150):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = splitter.split_text(text)

    enriched_chunks = []

    current_section = "UNKNOWN"
    current_product = "UNKNOWN"

    for chunk in chunks:

        # Section detection
        if "PERSONAL : LOAN PRODUCTS" in chunk:
            current_section = "PERSONAL_LOAN_PRODUCTS"

        # Product detection (simple heuristic)
        if "Personal Loan" in chunk:
            current_product = "PERSONAL_LOAN"
        elif "Home Loan" in chunk:
            current_product = "HOME_LOAN"
        elif "Gold Loan" in chunk:
            current_product = "GOLD_LOAN"
        elif "Education Loan" in chunk:
            current_product = "EDUCATION_LOAN"
        elif "Pension Loan" in chunk:
            current_product = "PENSION_LOAN"

        enriched_chunks.append({
            "text": chunk,
            "section": current_section,
            "product": current_product
        })

    return enriched_chunks

