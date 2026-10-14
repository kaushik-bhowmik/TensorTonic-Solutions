def local_vjp(operation: str, inputs: list, output: float, upstream_gradient: float) -> list:
    """
    Returns a list of float gradient contributions in input order.
    """
    upstream_gradient = float(upstream_gradient)
    if operation=="add":
        return [upstream_gradient, upstream_gradient]
    elif operation=="mul":
        return [upstream_gradient*inputs[1], upstream_gradient*inputs[0]]
    else:
        return [upstream_gradient*(1-output**2)]
