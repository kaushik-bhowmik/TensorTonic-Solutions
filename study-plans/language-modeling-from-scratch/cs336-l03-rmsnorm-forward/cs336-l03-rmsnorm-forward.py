import torch

def rmsnorm(x: torch.Tensor, g: torch.Tensor, epsilon: float) -> torch.Tensor:
    """
    Returns the RMS-normalized tensor with the same shape and dtype as x.
    """
    num = x*g 
    this = x*x 
    den = torch.sqrt(torch.mean(this,dim=-1,keepdim=True)+epsilon)
    rmsn = num /den 
    return rmsn 
