import numpy as np
from llama_index.embeddings.nvidia import NVIDIAEmbedding

model = NVIDIAEmbedding(model="nvidia/nemotron-3.5-embed-1b", truncate="END")

sentences = [
    "High blood sugar can damage your kidneys.",
    "Hyperglycemia harms the kidneys over time.",
    "My cat likes to sleep in the sun.",
]
vecs = [np.array(model.get_text_embedding(s)) for s in sentences]
print("Each fingerprint has", len(vecs[0]), "numbers")
print("The first 5 numbers:", vecs[0][:5].round(3))

def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

print("sugar vs hyperglycemia:", round(cosine(vecs[0], vecs[1]), 3))
print("sugar vs cat:          ", round(cosine(vecs[0], vecs[2]), 3))