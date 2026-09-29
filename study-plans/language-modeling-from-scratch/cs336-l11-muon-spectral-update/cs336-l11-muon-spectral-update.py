import torch

def muon_spectral_update(
    parameter: torch.Tensor, gradient: torch.Tensor,
    previous_momentum: torch.Tensor, momentum_coefficient: int | float,
    learning_rate: int | float,
) -> dict:
    """
    Returns a dict of tensors: new_parameter, new_momentum, orthogonalized_update.
    """
    pass
    Bt = momentum_coefficient * previous_momentum + gradient 
    Bt_float = Bt.float()
    U, S, Vh = torch.linalg.svd(Bt_float, full_matrices=False)
    Ot = (U @ Vh).to(Bt.dtype)
    #U, S, Vh = torch.linalg.svd(Bt, full_matrices=False) ; Ot = U @ Vh
    #Ot = U@S.T
    Wt = parameter - learning_rate *Ot 
    return {"new_parameter": Wt,"new_momentum": Bt ,"orthogonalized_update":Ot}
