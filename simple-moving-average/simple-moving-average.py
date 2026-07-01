def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    window =0 ; 
    res=[]
    for i in range(window_size):
        window+=values[i]
    entry = window/window_size 
    res.append(entry)
    for i in range(window_size, len(values)):
        window-=values[i-window_size]
        window+=values[i]
        print(window)
        res.append(window/window_size)
    return res