import torch
import torch.nn.functional as F

def sgns_loss(center_vec: torch.Tensor, pos_vec: torch.Tensor, neg_vecs: torch.Tensor) -> torch.Tensor:
    """
    Returns a scalar torch.Tensor: the SGNS loss.
    """
    # YOUR CODE HERE
    f = F.softplus(-center_vec @pos_vec) #-F.softmax(center_vec @pos_vec)
    s = torch.sum(F.softplus(neg_vecs @ center_vec))
    return f+s 
