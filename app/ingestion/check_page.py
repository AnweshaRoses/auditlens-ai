import pymupdf


PDF_PATH = "data/raw/adityatb.pdf"

doc = pymupdf.open(PDF_PATH)

page = doc[10]  # Page 11

print("Page number:", 11)
print("Text:", repr(page.get_text("text")))
print("Images:", len(page.get_images(full=True)))

doc.close()