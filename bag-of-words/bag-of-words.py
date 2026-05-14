import numpy as np
from collections import defaultdict
def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    rec = defaultdict(int)
    res = [0 for x in range(len(vocab))]
    index=0
    for each in vocab:
        rec[each]=0
    for each in tokens:
        if each in rec.keys():
            rec[each]+=1
    out = np.array(list(rec.values()),dtype=int)
    return out