import torch

def attention_scores(q: torch.Tensor, k: torch.Tensor, num_heads: int) -> torch.Tensor:
    """
    Returns scores of shape (batch, heads, query_length, key_length).
    """
    B, T, D = q.shape 
    dhead = D//num_heads
    S_q = q.shape[1]
    S_k = k.shape[1]
    query = q.view(B, S_q, num_heads, dhead)
    key = k.view(B, S_k, num_heads, dhead)
    query = query.transpose(1,2)
    key = key.transpose(1,2)
    attn = (query@key.transpose(-2, -1))/dhead**0.5 
    return attn 
