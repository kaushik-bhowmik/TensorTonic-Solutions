import numpy as np

def unet_encoder_block(x: np.ndarray, out_channels: int) -> tuple:
    """
    Returns (pool_out, skip_out) as zero arrays with correct shapes.
    """
    # Your implementation here
    ps = np.zeros((x.shape[0], (x.shape[1]-4)//2, (x.shape[2]-4)//2, out_channels)) #; ps = np.asarray(ps)
    ss = np.zeros((x.shape[0], (x.shape[1]-4), (x.shape[2]-4), out_channels))
    return (ps, ss)
