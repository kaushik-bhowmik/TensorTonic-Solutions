import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows = len(A) ; cols = len(A[0])
    res= [[0]*rows for each in range(cols)]
    #print("R:",res)
    for row in range(rows):
        for col in range(cols):
            res[col][row]=A[row][col]
    #print(res)
    return np.array(res) 
