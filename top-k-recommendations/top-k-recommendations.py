from collections import defaultdict
def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    res= []
    for i in range(len(scores)):
        if i not in rated_indices:
            res.append([scores[i],i])
    ans =[]
    res.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(res)):
        if k==0:
            break
        ans.append(res[i][1])
        k-=1
        
    return ans