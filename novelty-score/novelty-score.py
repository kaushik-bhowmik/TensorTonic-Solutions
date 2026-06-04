import numpy as np 
def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here
    item_counts = np.array(item_counts,dtype=float)
    this = np.log2(item_counts/n_users)
    this = - np.mean(this)
    return this 
    