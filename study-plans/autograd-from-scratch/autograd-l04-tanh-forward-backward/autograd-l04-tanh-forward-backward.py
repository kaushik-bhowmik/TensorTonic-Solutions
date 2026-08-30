import torch

def tanh_forward_backward(x, upstream_gradient):
    """
    Returns: tanh output and its upstream-scaled input gradient
    """
    #x = x.to(torch.float64) ; upstream_gradient = upstream_gradient.to(torch.float64)
    #out = (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))
    #lx = upstream_gradient * (1-out**2)
    out = torch.tanh(x)
    lx = upstream_gradient * (1 - out**2)

    return out, lx
