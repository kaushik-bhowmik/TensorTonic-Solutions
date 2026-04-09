def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    series = np.array(series)
    #res = np.zeros_like(series)
    res = (series[1:] - series[:-1])/series[:-1]
    res[np.isinf(res)] = 0
    return res 

    