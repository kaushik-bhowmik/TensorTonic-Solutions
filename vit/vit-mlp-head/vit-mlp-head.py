import numpy as np

def classification_head(encoder_output: np.ndarray,
                        W_head: np.ndarray) -> np.ndarray:
    """
    Returns float64 class logits with shape (B, C).
    """
    this = encoder_output[:,0,:] #[0] 
    mean = np.mean(this,axis=-1,keepdims=True)
    var = np.var(this,axis=-1,keepdims=True)
    hnorm = (this - mean) / (np.sqrt(var +10**-6))
    logits = hnorm@W_head
    #print(logits[0])
    #logits = logits[0].reshape(encoder_output.shape[0],encoder_output.shape[1])
    return logits