def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    wt=[returns[x] for x in range(len(returns))]
    for i in range(len(returns)):
        if i==0:
            wt[i] = 1+returns[i]
        else:
            wt[i] = wt[i-1]* (1+returns[i]) 
            #wt[i] = wt[i]-1
    for i in range(len(returns)):
        wt[i] = wt[i]-1
    return wt 