from collections import defaultdict
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    rec = defaultdict(int)
    for each in values:
        rec[each]+=(1/len(values))
    ans =[]
    for each in values:
        ans.append(rec[each])
    return ans 
        