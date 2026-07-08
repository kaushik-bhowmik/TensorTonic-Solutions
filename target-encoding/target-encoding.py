from collections import Counter, defaultdict
def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    count = Counter(categories)
    #print(count)
    tot = defaultdict(int)
    for i in range(len(categories)):
        tot[categories[i]]+=targets[i]
    #print(tot)
    res =[]
    for i in range(len(categories)):
        res.append(tot[categories[i]]/count[categories[i]])
    return res