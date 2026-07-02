def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    rec= set()
    for each in recommendations:
        for i in range(len(each)):
            rec.add(each[i])
    return len(rec)/n_items 