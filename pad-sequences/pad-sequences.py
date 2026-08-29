import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len==None:
        maxi = float("-inf")
        for each in seqs:
            maxi = max(maxi, len(each))
    else:
        maxi = max_len 
    for i, each in enumerate(seqs):
        if len(each)>maxi:
            seqs[i] = seqs[i][:maxi] 
        elif len(each)<maxi:
            this = [pad_value] * (maxi-len(each))
            seqs[i].extend(this)
    if not seqs:
        arr = np.empty((0, 0), dtype=int)
        return arr 
    num = np.array(seqs,dtype=int)
    return num 
    