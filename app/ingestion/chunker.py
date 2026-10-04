def chunk_pages(
    pages: list[dict],
    chunk_size: int = 1200,
    overlap: int = 200,
) -> list[dict]:

    chunks = []

    for page in pages:

        text = page["text"]

        start = 0
        chunk_number = 1

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append(
                    {
                        "chunk_id": (
                            f"{page['document']}"
                            f"_p{page['page']}"
                            f"_c{chunk_number}"
                        ),
                        "document": page["document"],
                        "page": page["page"],
                        "source_type": page["source_type"],
                        "text": chunk_text,
                    }
                )

            start += chunk_size - overlap
            chunk_number += 1

    return chunks