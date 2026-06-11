import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    #rs = set(rater1)
    rater1 = np.array(rater1,dtype=float) ; rater2 = np.array(rater2,dtype=float)
    po = np.sum(rater1==rater2) / len(rater1)
    #print(po)
    #pe = [0 for i in range(len(rs))]
    unique_values1, counts1 = np.unique(rater1, return_counts=True)
    unique_values2, counts2 = np.unique(rater2, return_counts=True)
    #for each in 
    pe = (counts1/len(rater1)) *(counts2/len(rater1)) 
    pes = np.sum(pe)
    #print(pes)
    if pes==1:
        return 1
    out = (po-pes)/(1-pes)
    return out