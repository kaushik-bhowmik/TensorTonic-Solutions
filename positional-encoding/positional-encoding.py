import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pe = np.zeros((seq_len,d_model), dtype=float)
    for pos in range(seq_len):
        for i in range(d_model):
            k=i//2
            if i%2==0:
                pe[pos][i] = np.sin(pos/(base**(2*k/d_model)))
            else:
                pe[pos][i] = np.cos(pos/(base**(2*k/d_model)))
    return pe 
    