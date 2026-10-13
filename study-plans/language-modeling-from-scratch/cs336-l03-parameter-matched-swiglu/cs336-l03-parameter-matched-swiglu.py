import torch
import math 
def parameter_matched_swiglu(
    x: torch.Tensor, w_g: torch.Tensor, w_v: torch.Tensor,
    w_o: torch.Tensor, base_params: int,
) -> dict:
    """
    Returns output, hidden_width, and parameter_count in a dictionary.
    """
    H = w_g.shape[1]
    h = min(H,max(1,math.floor((base_params/(3*x.shape[-1]))+0.5)))
    def silu(z):
        this = z/(1+torch.exp(-z))
        return this 
    temp  = silu(x@w_g[:,:h])
    out = (temp *(x@w_v[:,:h])) @w_o[:h,:]
    #out = out[:,:h]
    return {"output":out , "hidden_width":h, "parameter_count":3*w_g.shape[0]*h} 
