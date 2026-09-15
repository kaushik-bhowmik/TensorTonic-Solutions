import numpy as np

def bert_embeddings(token_ids: np.ndarray, segment_ids: np.ndarray,
                    token_embeddings: np.ndarray, position_embeddings: np.ndarray,
                    segment_embeddings: np.ndarray) -> np.ndarray:
    """
    Returns the float64 BERT input embeddings with shape (B, S, H).
    """
    B, S = token_ids.shape

    token_vectors = token_embeddings[token_ids]          # (B, S, H)
    position_vectors = position_embeddings[:S]          # (S, H)
    segment_vectors = segment_embeddings[segment_ids]   # (B, S, H)

    out = token_vectors + position_vectors + segment_vectors

    return out.astype(np.float64)