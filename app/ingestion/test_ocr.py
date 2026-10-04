import pymupdf
import pytesseract
from PIL import Image
import io


PDF_PATH = "data/raw/adityatb.pdf"


doc = pymupdf.open(PDF_PATH)

page = doc[10]  # Page 11

# Render the PDF page as an image
pix = page.get_pixmap(dpi=150)

image_bytes = pix.tobytes("png")

image = Image.open(io.BytesIO(image_bytes))

# Run OCR
text = pytesseract.image_to_string(image)

print("OCR output:")
print(text[:3000])

doc.close()