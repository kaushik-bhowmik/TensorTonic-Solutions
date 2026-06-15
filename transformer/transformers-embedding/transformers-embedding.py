import torch
import torch.nn as nn
import math

def create_embedding_layer(vocab_size: int, d_model: int) -> nn.Embedding:
    """
    Create an embedding layer.
    """
    # Your code here
    embed  = nn.Embedding(num_embeddings=vocab_size, embedding_dim=d_model)
    return embed 

def embed_tokens(embedding: nn.Embedding, tokens: torch.Tensor, d_model: int) -> torch.Tensor:
    """
    Convert token indices to scaled embeddings.
    """
    # Your code here
    out = embedding.weight[tokens]* torch.sqrt(torch.tensor(d_model))
    print(out.shape)
    return out 