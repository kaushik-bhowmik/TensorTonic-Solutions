import numpy as np
from collections import Counter
def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    rec = Counter(y_train)
    val = max(rec.values())
    this = float("inf")
    for each in rec.keys():
        if rec[each]==val and this>each:
            this =each
    out = np.ones_like(X_test)*this
    return out 