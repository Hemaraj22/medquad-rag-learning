# 🩺 MedQuAD RAG — a hands-on rebuild

I'm rebuilding a **hybrid-search medical Q&A system** piece by piece, so that I understand every technology in it, not just run it.

The starting point is [JAGAN666/medquad-rag-api](https://github.com/JAGAN666/medquad-rag-api) (MIT). Its README is kept here as [ORIGINAL_README.md](ORIGINAL_README.md), and its commit history is preserved. Everything after that history is my own work.

The system answers medical questions with **verbatim** text from ~17,000 NIH question-and-answer pairs ([MedQuAD](https://github.com/abachaa/MedQuAD)). It retrieves answers rather than generating them, so it cannot make anything up.

---

## 🔧 What I changed from the original

| Change | Why |
|---|---|
| **Switched the embedding model** to `nvidia/nemotron-3.5-embed-1b` | The original `llama-3.2-nv-embedqa-1b-v2` was retired by NVIDIA on 2026-05-18 and now returns `410 Gone`. |
| **Adding a true Reciprocal Rank Fusion function** *(Step 8, in progress)* | The original README says it uses RRF, but `llama-index-vector-stores-qdrant` 0.9.1 defaults to *relative score fusion*. I'm writing an RRF function to plug in with `hybrid_fusion_fn`. |
| **Wrote one lesson script per technology** | Each one isolates a single idea, so it can be run and understood on its own. |

---

## 🧭 Learning path

| Step | Script | Technology | What it shows |
|---|---|---|---|
| 1 | — | Git, Python `venv`, pip | Project setup and isolated dependencies |
| 2 | [lesson2_xml.py](lesson2_xml.py) | XML, `ElementTree` | Parsing MedQuAD documents into Q&A pairs and metadata |
| 3 | — | API keys, environment variables | Keeping secrets in `.env`, outside the code |
| 4 | [lesson4_embeddings.py](lesson4_embeddings.py) | NVIDIA embeddings, NumPy | Dense vectors and cosine similarity: "high blood sugar" ≈ "hyperglycemia" (0.88) |
| 5 | [lesson5_bm25.py](lesson5_bm25.py) | FastEmbed BM25 | Sparse keyword vectors, stopwords, and why keywords alone miss synonyms |
| 6 | [lesson6_rrf.py](lesson6_rrf.py) | Reciprocal Rank Fusion | Merging two ranked lists by position, and the effect of `k` |
| 7 | [lesson7_qdrant.py](lesson7_qdrant.py) | Qdrant | Collections, points, payloads, upsert, and nearest-neighbor search |
| 8 | *in progress* | LlamaIndex | Hybrid retrieval over real MedQuAD data with my RRF function |
| 9 | *planned* | FastAPI, Pydantic | A REST API with a `/query` endpoint |
| 10 | *planned* | HTML, JavaScript `fetch` | A web front end |
| 11 | *planned* | Arize Phoenix | Tracing each retrieval step |
| 12 | *planned* | Docker, Qdrant Cloud, Cloud Run | Containerizing and deploying |

---

## 🏗 How it works

```
Phase A: indexing (once)
  MedQuAD XML ─▶ Q&A documents ─▶ dense vectors (NVIDIA) + sparse vectors (BM25) ─▶ Qdrant

Phase B: answering (every question)
  question ─▶ dense search + sparse search ─▶ Reciprocal Rank Fusion ─▶ verbatim NIH answers
```

---

## ▶️ Running the lessons

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
git clone https://github.com/abachaa/MedQuAD.git

# .env must contain NVIDIA_API_KEY=nvapi-... (free key from build.nvidia.com)
set -a; source .env; set +a

python lesson2_xml.py
```

---

## 🛠 Tech stack

Python · LlamaIndex · Qdrant · NVIDIA NIM embeddings · FastEmbed (BM25) · Hybrid search · Reciprocal Rank Fusion · FastAPI · Docker
