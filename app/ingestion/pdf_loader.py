import io
from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image


def extract_pages_from_pdf(file_path: str) -> list[dict]:
    """
    Extract text from every PDF page.

    Uses normal PDF text extraction when available.
    Falls back to OCR for scanned/image-based pages.
    """

    pdf_path = Path(file_path)

    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        # First attempt: extract the PDF's existing text layer
        text = page.get_text("text").strip()

        source_type = "text"

        # Second attempt: OCR if no text layer exists
        if not text:

            source_type = "ocr"

            pix = page.get_pixmap(dpi=150)

            image_bytes = pix.tobytes("png")

            image = Image.open(io.BytesIO(image_bytes))

            text = pytesseract.image_to_string(image).strip()

        pages.append(
            {
                "document": pdf_path.name,
                "page": page_number,
                "text": text,
                "source_type": source_type,
            }
        )

    document.close()

    return pages