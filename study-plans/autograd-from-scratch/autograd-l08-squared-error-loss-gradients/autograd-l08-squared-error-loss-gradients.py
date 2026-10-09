import torch

def squared_error_loss_gradients(predictions: torch.Tensor, targets: torch.Tensor) -> tuple:
    """
    Returns a scalar loss tensor and a prediction-shaped gradient tensor.
    """
    """if predictions.numel() == 0 or targets.numel()==0:
        return (0, torch.zeros_like(predictions))"""
    L = torch.sum((predictions-targets)**2)
    grad = 2*(predictions-targets)
    return (L,grad)
    
