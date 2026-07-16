def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    res= []
    for each in X:
        res.append(each)
        this =[]
        for i in range(len(each)):
            for j in range(i+1,len(each)):
                this.append(each[i]*each[j])
        res[-1].extend(this)
    return res 