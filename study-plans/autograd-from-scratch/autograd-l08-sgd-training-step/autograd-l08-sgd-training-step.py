import torch

def sgd_training_step(inputs: torch.Tensor, targets: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor, learning_rate: float) -> tuple:
    """
    Returns old loss, new loss, updated weights, updated bias, weight gradients, and bias gradient.
    """
    #input = torch.tensor(...)
    #targets = torch.tensor(...)
    
    w = weights.clone()
    b = bias.clone()
    pi = torch.tanh(inputs@w+b)
    Lold = torch.sum((pi-targets)**2)
    ## Grad calcualtion
    dldw = inputs.T@(2*(pi-targets)*(1-pi**2)  )
    dldb = 2*(pi-targets) @(1-pi**2).T
    ##Update
    w -= learning_rate * dldw 
    b -= learning_rate * dldb 
    pinew = torch.tanh(inputs@w+b)
    Lnew = torch.sum((pinew-targets)**2)
    return (Lold,Lnew,w,b,dldw,dldb)
