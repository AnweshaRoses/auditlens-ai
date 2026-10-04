import pymupdf


PDF_PATH = "data/raw/adityatb.pdf"

doc = pymupdf.open(PDF_PATH)

print(f"Actual PDF pages: {len(doc)}")

for page_number, page in enumerate(doc, start=1):

    text = page.get_text("text")

    print(
        f"Page {page_number:2d} | "
        f"characters extracted: {len(text)}"
    )

doc.close()
