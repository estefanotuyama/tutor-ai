from sentence_transformers import SentenceTransformer

model_name = 'all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

def generate_embeddings(documents):
    return model.encode(documents)
