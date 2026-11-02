def memory_accountant(
    param_shapes: list[list[int]], param_bytes_per_element: int,
    grad_bytes_per_element: int, activation_shapes: list[list[int]],
    activation_bytes_per_element: int, optimizer: str,
    optimizer_bytes_per_element: int,
) -> dict:
    """
    Returns integer byte counts for parameters, gradients, activations, optimizer_state, and total.
    """
    ### Parameters
    param=0
    for layer in param_shapes:
        this = 1
        for each in layer:
            this = this * each 
        param+=this 
    ## Gradient
    grad = param 
    ## activation 
    act=0 
    for layer in activation_shapes:
        this =1 
        for each in layer:
            this = this* each 
        act+=this 
    ## Optimizer 
    opt = param 
    if optimizer=="adam":
        mul = 2
    elif optimizer=="adagrad":
        mul = 1
    else:
        mul=0
    ### Final Answer
    ans = param * param_bytes_per_element +grad* grad_bytes_per_element  + act * activation_bytes_per_element + mul *opt * optimizer_bytes_per_element
    return {"parameters": param * param_bytes_per_element, "gradients":grad* grad_bytes_per_element ,"activations":act * activation_bytes_per_element,"optimizer_state":mul *opt * optimizer_bytes_per_element,"total":ans }
        
