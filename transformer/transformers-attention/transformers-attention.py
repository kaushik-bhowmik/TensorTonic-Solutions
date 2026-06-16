import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    # Your code here
    x = Q @K.transpose(-2, -1) / torch.sqrt(torch.tensor(Q.size(2)))
    out =  torch.softmax(x, dim=-1) @ V 
    return out 