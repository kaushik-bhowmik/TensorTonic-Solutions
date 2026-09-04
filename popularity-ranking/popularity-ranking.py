def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here
    res =[]
    for avr,v_c in items:
        this = (v_c/(v_c+min_votes))* avr + (min_votes/(v_c+ min_votes))*global_mean
        res.append(this)
    return res 