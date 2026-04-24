def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for o in range(order):
        res= []
        for i in range(1, len(series)):
            res.append(series[i]-series[i-1])
        series =res 
    return res 
        