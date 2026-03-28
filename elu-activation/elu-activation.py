def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    for i in range(len(x)):
        if x[i]>0:
            continue 
        else:
            x[i] = alpha*(-1+math.e**x[i])
    return x
    