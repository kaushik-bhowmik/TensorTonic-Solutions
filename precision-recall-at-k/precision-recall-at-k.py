def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    rel_set = set(relevant) ; count=0
    for each in range(k):
        if recommended[each] in rel_set:
            count+=1
    return [count/k, count/len(relevant)]