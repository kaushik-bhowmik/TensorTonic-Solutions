from collections import deque 
def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    window = deque([])
    res =[]
    def get_val(window):
        this = len(window)//2
        if len(window)%2==0:
            f = this-1 ; s = this
            return (window[f]+window[s])/2
        else:
            return window[this]
    for i in range(window_size):
        window.append(values[i])
    this = list(window)
    this.sort()
    res.append(get_val(this))
    for i in range(window_size,len(values)):
        window.popleft()
        window.append(values[i])
        this = list(window)
        this.sort()
        res.append(get_val(this))   
    return res 