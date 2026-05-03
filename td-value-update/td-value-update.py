import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    #V = np.array(V)
    #Vn = V.copy()
    Vn = np.array(V, dtype=float).copy()
    delta = r + gamma * Vn[s_next] - Vn[s]
    Vn[s] = Vn[s] + alpha *delta 
    return Vn 