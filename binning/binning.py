def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    maxi = max(values) #max(max(values), num_bins-1)
    mini = min(values)
    w = (maxi - mini)/num_bins
    res= []
    
    if maxi == mini:
        return [0] * len(values)
    for i in range(len(values)):
        this = min((values[i]-mini)//w,num_bins -1)
        res.append(this)
    return res 
    