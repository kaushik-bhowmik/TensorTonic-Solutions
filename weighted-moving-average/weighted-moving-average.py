def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    #weights = np.asarray(weights,dtype=float)
    #values = np.asarray(values,dtype=float)
    w_total = sum(weights)
    print(w_total)
    res =[]
    for each in range(len(values)-len(weights)+1):
        temp =0
        for i in range(len(weights)):
            temp += weights[i] * values[each+i]
        res.append(temp/w_total)
    return res 
        