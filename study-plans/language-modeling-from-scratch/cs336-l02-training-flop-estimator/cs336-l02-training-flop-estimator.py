def flop_estimator(matmuls: list[list[int]], attention_flops: int = 0) -> dict:
    """
    Returns integer forward_flops, backward_flops, and total_flops in a dictionary.
    """
    forward=0; backward =ftotal=0
    for layer in matmuls:
        forward += 2*layer[0]*layer[1]*layer[2]
    forward +=attention_flops
    backward = 2*forward 
    ftotal = forward + backward 
    print(forward, backward,ftotal)
    #return  {"forward_flops":96,"backward_flops":192,"total_flops":288}
    return {"forward_flops":forward, "backward_flops":backward, "total_flops":ftotal}
    
    
