import numpy as np

def scalar_expression_partials(a, b, c, h):
    """
    Returns: the expression value and its three numerical partial derivatives
    """
    # Ensure 64-bit floating-point arithmetic
    a = np.float64(a)
    b = np.float64(b)
    c = np.float64(c)
    h = np.float64(h)

    def f(a, b, c):
        return a * b + c

    # Baseline
    d = f(a, b, c)

    # Forward differences
    da = (f(a + h, b, c) - d) / h
    db = (f(a, b + h, c) - d) / h
    dc = (f(a, b, c + h) - d) / h

    return (float(d), float(da), float(db), float(dc))
