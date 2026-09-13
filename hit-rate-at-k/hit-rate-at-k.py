def hit_rate_at_k(recommendations: list, ground_truth: list, k: int) -> float:
    """
    Returns the fraction of users with a relevant item in their first k recommendations.
    """
    # Write code here
    hit =0
    for i, each in enumerate(recommendations):
        this = each[:k]
        if ground_truth[i][0] in this:
            hit+=1
    return hit/len(ground_truth)
        
        