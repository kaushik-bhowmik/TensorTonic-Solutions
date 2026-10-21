import numpy as np
#import math 
def patch_embed(image: np.ndarray, patch_size: int,
                W_proj: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """
    Returns float64 patch embeddings with shape (B, N, D).
    """
    B = image.shape[0] ; H = image.shape[1] ; W= image.shape[2] ; C = image.shape[3]
    N = np.floor(H/patch_size) *np.floor(W/patch_size)
    image = image[:, :H // patch_size * patch_size,
              :W // patch_size * patch_size, :]
    patches = image.reshape(
        B,
        H // patch_size, patch_size,
        W // patch_size, patch_size,
        C
    )
    patches = patches.transpose(0, 1, 3, 2, 4, 5)
    patches = patches.reshape(B, -1, patch_size * patch_size * C)
    zp = patches@W_proj + bias 
    return zp 