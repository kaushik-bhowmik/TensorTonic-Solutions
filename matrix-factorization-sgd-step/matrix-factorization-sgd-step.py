def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    U = np.array(U) ; V= np.array(V)
    e = r-np.dot(U,V)
    Unew = U +lr*(e*V-reg*U)
    Vnew = V +lr*(e*U-reg*V)
    return (Unew,Vnew)