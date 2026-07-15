import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    res= []
    for pos in range(seq_length):
        this =[]
        for i in range(d_model):
            if i%2==0:
                cal = pos/(10000**(2*i//2 *d_model**-1))
                this.append(np.sin(cal))
            else:
                cal = pos/(10000**(2*(i-1)//2 *d_model**-1))
                this.append(np.cos(cal))
        res.append(this)
    res = np.asarray(res)
    return res 