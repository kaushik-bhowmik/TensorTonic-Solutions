import numpy as np

def add_position_embedding(patches: np.ndarray,
                           pos_embed: np.ndarray) -> np.ndarray:
    """
    Returns the float64 tokens after adding position embeddings.
    """
    out = patches + pos_embed 
    return out 