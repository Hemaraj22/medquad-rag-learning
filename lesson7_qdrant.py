from qdrant_client import QdrantClient, models
from llama_index.embeddings.nvidia import NVIDIAEmbedding

embed = NVIDIAEmbedding(model="nvidia/nemotron-3.5-embed-1b", truncate="END")

# 1. Build a pretend shelf that lives only in memory
client = QdrantClient(":memory:")

# 2. Our three cards
cards = [
    "Asthma causes wheezing and coughing at night.",
    "Diabetes means your blood sugar is too high.",
    "Broken bones heal with a cast and rest.",
]
fingerprints = embed.get_text_embedding_batch(cards)

# 3. Make a shelf section (a "collection") sized for our fingerprints
client.create_collection(
    collection_name="toy_shelf",
    vectors_config=models.VectorParams(
        size=len(fingerprints[0]),
        distance=models.Distance.COSINE,
    ),
)

# 4. Put each card on the shelf: id + fingerprint + the card text
client.upsert(
    collection_name="toy_shelf",
    points=[
        models.PointStruct(id=i, vector=fp, payload={"text": card})
        for i, (card, fp) in enumerate(zip(cards, fingerprints))
    ],
)
print("Cards on the shelf:", client.count("toy_shelf").count)

# 5. Ask a question
question = "How do I fix a broken arm?"
q_fp = embed.get_query_embedding(question)
hits = client.query_points("toy_shelf", query=q_fp, limit=3).points

print("\nQuestion:", question)
for hit in hits:
    print(round(hit.score, 3), "->", hit.payload["text"])