import math
import torch

def densenet_channel_counts(stem_channels: int, growth_rate: int, block_layers, compression: float) -> torch.Tensor:
    """
    Returns a 1D int64 torch.Tensor of channel counts at each stage.
    """
    # YOUR CODE HERE
    res=[stem_channels]
    for i in range(len(block_layers)):
        res.append(res[-1]+block_layers[i]*growth_rate)
        if i!=len(block_layers)-1:
            res.append(math.floor(res[-1] * compression))
    t = torch.tensor(res,dtype = torch.int64)
    return t 
