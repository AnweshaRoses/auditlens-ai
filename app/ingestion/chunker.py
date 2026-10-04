def chunk_pages(
    pages: list[dict],
    chunk_size: int = 1200,
) -> list[dict]:

    chunks = []

    for page in pages:

        text = page["text"].strip()

        if not text:
            continue

        # Split text into paragraphs using blank lines
        paragraphs = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]

        current_chunk = ""
        chunk_number = 1

        for paragraph in paragraphs:

            # If adding this paragraph stays within the limit,
            # keep it in the current chunk.
            if len(current_chunk) + len(paragraph) + 1 <= chunk_size:

                if current_chunk:
                    current_chunk += "\n\n"

                current_chunk += paragraph

            else:

                # Save the current chunk
                if current_chunk:

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
                            "text": current_chunk,
                        }
                    )

                    chunk_number += 1

                # Start a new chunk with the current paragraph
                current_chunk = paragraph

        # Save final chunk from the page
        if current_chunk:

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
                    "text": current_chunk,
                }
            )

    return chunks