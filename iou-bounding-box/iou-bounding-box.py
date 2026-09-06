def iou(box_a: list, box_b: list) -> float:
    """
    Returns IoU as a float.
    """
    # Write code here
    Aa = abs(box_a[0]-box_a[2]) * abs(box_a[1]-box_a[3])
    Ab = abs(box_b[0]-box_b[2]) * abs(box_b[1]-box_b[3])
    xl = max(box_a[0], box_b[0])
    yt = max(box_a[1], box_b[1])
    xr = min(box_a[2], box_b[2])
    yb = min(box_a[3], box_b[3])
    Ai = max(0,xr-xl) * max(0,yb-yt)
    Au = Aa+Ab -Ai
    return Ai/Au 