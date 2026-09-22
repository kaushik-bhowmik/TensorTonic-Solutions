import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    # Write code here
    T = np.asarray(T) ; points = np.asarray(points)
    flag=False 
    if len(points.shape)!=1:
        points = points.reshape(-1,3)
    else:
        points = points.reshape(1, 3)
        flag = True 
    ones = np.ones((points.shape[0], 1))
    points_h = np.concatenate([points, ones], axis=1)
    out = points_h @ T.T 
    out = out[:, :3]
    if flag==True:
        out = out.reshape(3)
    return out 