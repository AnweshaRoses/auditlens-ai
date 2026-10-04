# AuditLens AI

Enterprise-style RAG system for answering questions from
financial and audit documents with page-level citations.

## Architecture

PDF
→ Text Extraction / OCR
→ Page-aware Chunking
→ Embeddings
→ Retrieval
→ Reranking
→ LLM
→ Answer + Citations

## Retrieval Evolution

| Version | Retrieval Strategy | Recall@5 |
|---|---|---:|
| V1 | Dense FAISS | TBD |
| V2 | Improved Chunking | TBD |
| V3 | Hybrid Retrieval | TBD |
| V4 | Reranking | TBD |
| V5 | Tuned Pipeline | TBD |

## V1 Baseline

- Embedding model: `all-MiniLM-L6-v2`
- Vector store: FAISS
- Chunk size: 1200 characters
- Chunk overlap: 200 characters
- Top-k: 5