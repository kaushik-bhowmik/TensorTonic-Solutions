import torch

def neuron_gradient_check(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor, h: float) -> tuple:
    """
    Returns five tensors: analytic/numerical weight gradients, analytic/numerical bias gradients, maximum error.
    """
    y = torch.tanh(weights@inputs+bias)
    this = y*y 
    dy_dw = (1-this)*inputs 
    dy_db = 1-this 
    gi_num = torch.empty_like(weights)

    for i in range(weights.numel()):
        weights_perturbed = weights.clone()
        weights_perturbed[i] += h

        y_perturbed = torch.tanh(weights_perturbed @ inputs + bias)
        gi_num[i] = (y_perturbed - y) / h
    gb_num = (torch.tanh((weights)@inputs+bias+h) - y)/h
    diffw = torch.abs(dy_dw-gi_num)
    diffb = torch.abs(dy_db-gb_num)
    if weights.numel() == 0:
        diff = diffb.max()
    else:
        diff = max(diffw.max(),diffb.max())
    return (dy_dw,gi_num, dy_db,gb_num,diff)
