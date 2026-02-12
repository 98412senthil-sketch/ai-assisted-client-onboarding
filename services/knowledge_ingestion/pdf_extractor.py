def extract_pdf_text(path):
    from pypdf import PdfReader

    reader = PdfReader(path)
    full_text = ""

    # Skip first 3 pages (cover + foreword)
    for i, page in enumerate(reader.pages):
        if i < 3:
            continue
        full_text += page.extract_text() + "\n"

    cleaned = clean_text(full_text)

    return cleaned

 
def clean_text(text):
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Remove marketing/footer noise
        if "Follow us" in line:
            continue
        if "Scan to Download" in line:
            continue
        if "bank.sbi" in line:
            continue
        if line.isdigit():  # remove page numbers
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)