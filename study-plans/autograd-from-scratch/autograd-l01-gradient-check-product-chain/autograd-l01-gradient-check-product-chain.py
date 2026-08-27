import numpy as np
"""
def gradient_check_product_chain(a, b, c, f, h):
    a = np.float64(a)
    b = np.float64(b)
    c = np.float64(c)
    h = np.float64(h)
    f = np.float64(f)
    e = a*b +c ; L =e*f 
    ## Analytic ## abf+ cf
    la = b*f
    lb = a*f 
    lc = f 
    lf = a*b + c
    L_a = [la,lb,lc,lf]
    ## Numerical gradients
    lah = (a+h)*b*f+ c*f ; sa = (lah - L)/h
    lbh = a*(b+h)*f+ c*f ; sb = (lbh - L)/h
    lch = a*b*f+ (c+h)*f ; sc = (lch - L)/h
    lfh = a*b*(f+h)+ c*(f+h) ; sf = (lfh - L)/h
    L_n = [sa,sb,sc,sf]
    diff = -float("inf")
    for i in range(len(L_n)):
        diff = max(diff, abs(L_n[i]-L_a[i]))
    return (L,L_a, L_n, diff)"""
import numpy as np

def gradient_check_product_chain(a, b, c, f, h):
    a = np.float64(a)
    b = np.float64(b)
    c = np.float64(c)
    f = np.float64(f)
    h = np.float64(h)

    def loss(a, b, c, f):
        e = a * b + c
        return e * f

    # Original loss
    L = loss(a, b, c, f)

    # Analytic gradients
    analytic = [
        b * f,
        a * f,
        f,
        a * b + c
    ]

    # Forward differences
    numerical = [
        (loss(a + h, b, c, f) - L) / h,
        (loss(a, b + h, c, f) - L) / h,
        (loss(a, b, c + h, f) - L) / h,
        (loss(a, b, c, f + h) - L) / h
    ]

    # Maximum absolute disagreement
    max_diff = max(
        abs(n - a)
        for n, a in zip(numerical, analytic)
    )

    return (
        float(L),
        [float(x) for x in analytic],
        [float(x) for x in numerical],
        float(max_diff)
    )