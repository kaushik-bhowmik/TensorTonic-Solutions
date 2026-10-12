import torch

def gradient_accumulation_step(
    param: torch.Tensor, microbatch_inputs: list[torch.Tensor],
    microbatch_targets: list[torch.Tensor], lr: float,
) -> dict:
    """
    Returns new_param and full_grad tensors in a dictionary.
    """
    dldw = 0 ; count=0
    for ub,y in zip(microbatch_inputs,microbatch_targets):
        #dldw+= 2* ub.T@(ub.T@param-y)
        dldw += 2 * ub.T @ (ub @ param - y)
        count += y.numel()
    dldw = dldw/count 
    param_new = param - lr * dldw 
    return {"new_param":param_new, "full_grad":dldw} 
