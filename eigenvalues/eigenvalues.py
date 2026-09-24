import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    A = np.asarray(matrix)
    ev = np.linalg.eigvals(A)
    sorted_arr = np.sort(ev)
    return sorted_arr 