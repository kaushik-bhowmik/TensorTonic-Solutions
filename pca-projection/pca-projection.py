import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X)
    Xc = X - np.mean(X,axis = 0,keepdims=True)
    #cov = np.cov(X, rowvar=True, bias=False, ddof=1)
    #cov = np.cov(X, rowvar=True, bias=False, ddof=1)
    cov = np.cov(X, rowvar=False, ddof=1)
    ##import numpy as np
    
    # C: (D, D) covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    
    # Sort eigenvalues in descending order
    indices = np.argsort(eigenvalues)[::-1]
    
    eigenvalues = eigenvalues[indices]
    eigenvectors = eigenvectors[:, indices]
    
    # Select top-k eigenvectors
    top_k_eigenvalues = eigenvalues[:k]
    top_k_eigenvectors = eigenvectors[:, :k]
    ####
    Xproj = Xc@top_k_eigenvectors 
    return Xproj 