import numpy as np

# Define a toy sentence with 4 words (excluding stopwords for simplicity)
words = ["cat", "ate", "fish"]

# Assign simple word embeddings (random for now)
embedding_dim = 3  # Small embedding size for simplicity
np.random.seed(42)  # For reproducibility

word_embeddings = np.random.rand(len(words), embedding_dim)
print("Word Embeddings:\n", word_embeddings)


# Initialize weight matrices for Q, K, and V (random)
W_q = np.random.rand(embedding_dim, embedding_dim)
W_k = np.random.rand(embedding_dim, embedding_dim)
W_v = np.random.rand(embedding_dim, embedding_dim)

# Compute Q, K, and V vectors
Q = word_embeddings @ W_q
K = word_embeddings @ W_k
V = word_embeddings @ W_v

print("Query (Q):\n", Q)
print("Key (K):\n", K)
print("Value (V):\n", V)

# Compute raw attention scores (QK^T)
attention_scores = Q @ K.T  

print("Raw Attention Scores:\n", attention_scores)

# Apply softmax
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

attention_weights = softmax(attention_scores)

print("Attention Weights:\n", attention_weights)

# Multiply attention weights by value vectors
attention_output = attention_weights @ V

print("Final Attention Output:\n", attention_output)

# Print results
print("Word Embeddings:\n", word_embeddings)
print("\nQuery (Q):\n", Q)
print("\nKey (K):\n", K)
print("\nValue (V):\n", V)
print("\nAttention Scores:\n", attention_scores)
print("\nAttention Weights:\n", attention_weights)
print("\nFinal Attention Output:\n", attention_output)
