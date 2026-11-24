from fastembed import SparseTextEmbedding

bm25 = SparseTextEmbedding(model_name="Qdrant/bm25")

docs = [
    "High blood sugar can damage your kidneys.",
    "Hyperglycemia harms the kidneys over time.",
]
for text, emb in zip(docs, bm25.embed(docs)):
    print(text)
    print("   word ids:", emb.indices.tolist())
    print("   weights: ", emb.values.round(2).tolist())

q = list(bm25.query_embed("blood sugar"))[0]
print("\nQuestion 'blood sugar' word ids:", q.indices.tolist())

for text, emb in zip(docs, bm25.embed(docs)):
    shared = set(q.indices.tolist()) & set(emb.indices.tolist())
    print(f"Words shared with '{text}': {len(shared)}")