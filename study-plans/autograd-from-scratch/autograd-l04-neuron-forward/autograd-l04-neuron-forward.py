import torch

def neuron_forward(inputs, weights, bias):
    """
    Returns: scalar preactivation and tanh output
    """
    pre = inputs@weights.T +bias 
    act = torch.tanh(pre)
    return pre, act
