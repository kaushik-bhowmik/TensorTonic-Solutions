import torch
import torch.nn.functional as F

def cbow_forward(context_ids: torch.Tensor, target_id: int, W_in: torch.Tensor, W_out: torch.Tensor) -> torch.Tensor:
    """
    Returns a scalar torch.Tensor: the CBOW cross-entropy loss for predicting target_id from the averaged context.
    """
    # YOUR CODE HERE
    f = W_in[context_ids]
    h = torch.mean(f,dim=0)
    logits = W_out @h 
    target = torch.zeros((logits.shape))   #torch.zeros((3, 4)) 
    target[target_id]=1
    loss = F.cross_entropy(logits, target)
    return loss 
