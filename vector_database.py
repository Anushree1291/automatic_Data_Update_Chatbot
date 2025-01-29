import faiss
import numpy as np

class VectorDatabase:
    def __init__(self, dimension=512):
        self.index = faiss.IndexFlatL2(dimension)
        self.articles = []  # To keep track of original content

    def add_embeddings(self, embeddings, articles):
        embedding_matrix = np.array(embeddings).astype('float32')
        self.index.add(embedding_matrix)
        self.articles.extend(articles)

    def query(self, query_embedding, k=3):
        query_vector = np.array([query_embedding]).astype('float32')
        _, indices = self.index.search(query_vector, k)
        return [self.articles[i] for i in indices[0]]
