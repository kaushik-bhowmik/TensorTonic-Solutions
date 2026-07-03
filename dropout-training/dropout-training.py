import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    def create_mask(shape, p, rng=None):
        rand = rng.random(shape) if rng is not None else np.random.random(shape)
        return rand >= p
    mask = create_mask(x.shape,p,rng)
    o = x*mask /(1-p)
    mask = mask/(1-p)
    mask = mask.astype(float)
    out = (o,mask)
    return out 
    #pass