def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """
    # Write code here
    res = [series[0]]
    bt = series[1] - series[0]
    for i, each in enumerate(series):
        if i==0:
            continue 
        else:
            lt =  alpha * each + (1-alpha) * (res[-1]+bt)
            bt = beta * (lt - res[-1]) + (1-beta) *bt  
            res.append(lt)
    return res 