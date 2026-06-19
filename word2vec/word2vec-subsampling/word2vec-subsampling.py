import torch

def subsample_keep_probs(counts: torch.Tensor, t: float = 1e-5) -> torch.Tensor:
    """
    Returns torch.Tensor of shape (vocab_size,) with the keep-probability for each word.
    """
    # YOUR CODE HERE
    tot = torch.sum(counts)
    freq = counts / tot 
    Pkeep = torch.minimum(torch.sqrt(t/freq), torch.tensor(1))
    return Pkeep 
    
    
