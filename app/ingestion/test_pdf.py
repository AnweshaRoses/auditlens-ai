from app.ingestion.pdf_loader import extract_pages_from_pdf
from app.ingestion.chunker import chunk_pages


PDF_PATH = "data/raw/adityatb.pdf"


pages = extract_pages_from_pdf(PDF_PATH)

chunks = chunk_pages(pages)

print(f"Pages: {len(pages)}")
print(f"Chunks: {len(chunks)}")

for page in pages:
    print(
        f"Page {page['page']:2d} | "
        f"Source: {page['source_type']:4s} | "
        f"Characters: {len(page['text'])}"
    )