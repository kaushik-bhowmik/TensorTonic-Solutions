import torch

def mlp_forward(inputs: torch.Tensor, weights: list[torch.Tensor], biases: list[torch.Tensor]) -> tuple:
    """
    Returns the final output tensor and a list of layer-output tensors.
    """
    h = inputs ; res=[]#;out =[]
    for weight,bias in zip(weights,biases):
        out = torch.tanh(weight@h+bias)
        h= out 
        res.append(out) 
    return (h,res)
        
        
        
