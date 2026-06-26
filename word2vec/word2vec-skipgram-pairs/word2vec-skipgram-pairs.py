import torch

def skipgram_pairs(token_ids: torch.Tensor, window: int) -> torch.Tensor:
    """
    Returns int64 torch.Tensor of shape (num_pairs, 2).
    """
    # YOUR CODE HERE
    res =[]
    for i in range(len(token_ids)):
        for j in range(max(0,i-window), min(len(token_ids)-1, i+window)+1):
            if i!=j:
                res.append([token_ids[i],token_ids[j]])
    if res==[]:
        return torch.zeros((0, 2), dtype=torch.int64)
    t = torch.tensor(res, dtype=int)
    return t