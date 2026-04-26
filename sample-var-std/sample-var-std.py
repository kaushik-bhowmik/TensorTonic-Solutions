import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x= np.array(x)
    mean = np.sum(x)/x.shape[0]
    print(mean) 
    this = x-mean
    s_s = np.sum(this*this)/(x.shape[0]-1)
    std =np.sqrt(s_s)
    return (s_s,std)
    