import torch

def scalar_neuron_module(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor, nonlinear: bool) -> torch.Tensor:
    """
    Returns a scalar tensor preserving the input dtype and device.
    """
    #a = bias + weights@inputs 
    a = bias + torch.sum(inputs * weights)
    if nonlinear==True:
        out = torch.tanh(a)
    else:
        out =a 
    return out  
