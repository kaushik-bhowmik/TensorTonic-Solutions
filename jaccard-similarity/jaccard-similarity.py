def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)
    inter = float(len(set_a & set_b))
    union = float(len(set_a | set_b))
    return inter/union if union!=0 else 0
    