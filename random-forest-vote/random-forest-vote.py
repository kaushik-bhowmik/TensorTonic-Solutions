from collections import defaultdict 
def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    res= []
    for col in range(len(predictions[0])):
        rec = defaultdict(int)
        for row in range(len(predictions)):
            rec[predictions[row][col]]+=1
        maxi = max(rec.values())
        for each in sorted(rec):
            if rec[each]==maxi:
                res.append(each)
                break 
        #res.append(ans)
    return res 
            