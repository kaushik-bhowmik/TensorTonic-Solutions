def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    res =[]
    for i in range(len(series)):
        temp =[]
        for each in lags:
            if i-each>=0:
                temp.append(series[i-each])
        if len(temp)==len(lags):
            res.append(temp)
    return res 