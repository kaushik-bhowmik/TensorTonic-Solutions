from collections import Counter, defaultdict 
def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    """
    v_indices= defaultdict(list)
    for i in range(len(values)):
        v_indices[values[i]].append(i+1)
    print(v_indices)"""
    r_values = sorted(values)
    ranks = defaultdict(list)
    for i in range(len(r_values)):
        ranks[r_values[i]].append(i+1)
    res= [0 for x in range(len(values))]
    for i in range(len(values)):
        res[i] = sum(ranks[values[i]])/len(ranks[values[i]])   
    return res 
    