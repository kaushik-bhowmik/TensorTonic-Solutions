import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.array(X, dtype=float)
    w= np.zeros(X.shape[1]) ; b= 0.0
    ##w = np.zeros(X.shape[1])  # shape (D,)
    for step in range(steps):
        logits = X @w +b ; out = _sigmoid(logits)
        loss = np.mean(y *np.log(out)+(1-y)*np.log(1-out))
        ## gradient descent performs and weight and bias update perform
        gradw = np.mean(X.T *(out-y))
        gradb = np.mean(out-y)
        w = w- lr* gradw ; b = b-lr* gradb
    return (w,b)