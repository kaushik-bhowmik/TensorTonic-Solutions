import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    Supports both single vectors and batches of embeddings.
    """
    anchor = np.array(anchor, dtype=float)
    positive = np.array(positive, dtype=float)
    negative = np.array(negative, dtype=float)
    
    # Calculate Squared Euclidean Distance
    # axis=-1 ensures we sum across the embedding dimensions, keeping batch rows separate
    d_pos = np.sum((anchor - positive) ** 2, axis=-1)
    d_neg = np.sum((anchor - negative) ** 2, axis=-1)
    
    # Compute loss
    loss = np.maximum(0.0, d_pos - d_neg + margin)
    
    # If a batch was passed, return the average loss of the batch
    return np.mean(loss)