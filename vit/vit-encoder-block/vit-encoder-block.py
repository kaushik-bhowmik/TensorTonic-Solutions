import numpy as np
def gelu(x):
    return 0.5 * x * (
        1 + np.tanh(
            np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)
        )
    )

def vit_encoder_block(x: np.ndarray, num_heads: int,
                      Wq: np.ndarray, Wk: np.ndarray, Wv: np.ndarray,
                      Wo: np.ndarray, W1: np.ndarray, W2: np.ndarray) -> np.ndarray:
    """
    Returns the float64 output of one pre-normalized ViT encoder block.
    """
    dh = x.shape[-1]//num_heads ; B = x.shape[0] ; N = x.shape[1] ; D = x.shape[2]
    ## Stage 1 Layer Normalization
    mean = np.mean(x,axis=-1,keepdims=True)
    var = np.var(x,axis=-1,keepdims=True)
    x_norm = (x-mean)/(np.sqrt(var + 1e-6))
    #x_norm = x.reshape(x.shape[0],x.shape[1],num_heads,dh)
    x_norm = x_norm.reshape(x.shape[0], x.shape[1], num_heads, dh)
    ## Stage 2 Attention
    query = (x_norm.reshape(B, N, D) @ Wq).reshape(B, N, num_heads, dh)
    key   = (x_norm.reshape(B, N, D) @ Wk).reshape(B, N, num_heads, dh)
    value = (x_norm.reshape(B, N, D) @ Wv).reshape(B, N, num_heads, dh)
    query = query.transpose(0, 2, 1, 3)
    key   = key.transpose(0, 2, 1, 3)
    value = value.transpose(0, 2, 1, 3)
    scores = query @ key.transpose(0, 1, 3, 2)
    scores = scores / np.sqrt(dh)
    scores = scores - np.max(scores, axis=-1, keepdims=True)
    weights = np.exp(scores)
    weights = weights / np.sum(weights, axis=-1, keepdims=True)
    attn = weights @ value
    attn = attn.transpose(0, 2, 1, 3).reshape(B, N, D)
    ## Stage 3 concatenate
    y = x + attn @ Wo
    #y = x + np.reshape(x.shape[0],x.shape[1],x.shape[2])@Wo #@@@@@@@@@
    ### Stage 4 output
    mean = np.mean(y,axis=-1,keepdims=True)
    var = np.var(y,axis=-1,keepdims=True)
    y_norm = (y-mean)/(np.sqrt(var + 1e-6)) 
    z = y + gelu(y_norm@W1)@W2
    return z 