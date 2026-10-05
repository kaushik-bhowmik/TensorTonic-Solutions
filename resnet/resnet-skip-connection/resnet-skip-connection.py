import numpy as np

def compute_gradient_with_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Returns the gradient propagated through residual Jacobians.
    """
    gradients_F = np.asarray(gradients_F)
    for gradient in gradients_F:
        I = np.eye(gradient.shape[0])
        x = x@(I+gradient)
    return x 

def compute_gradient_without_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Returns the gradient propagated through plain Jacobians.
    """
    gradients_F = np.asarray(gradients_F)
    for gradient in gradients_F:
        x = x@gradient 
    return x 