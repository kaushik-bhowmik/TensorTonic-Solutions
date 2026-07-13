def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    res= []
    for each in values:
        this =[]
        for i in range(degree+1):
            this.append(each**i)
        res.append(this)
    return res 
        