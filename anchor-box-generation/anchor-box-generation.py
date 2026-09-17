def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """
    # Write code here
    anchor =[]
    stride  = image_size / feature_size 
    for x in range(feature_size):
        for y in range(feature_size):
            cx  = (y+0.5) * stride 
            cy = (x+0.5) * stride 
            for s in scales:
                for r in aspect_ratios:
                    w = s* (r)**0.5 ; h = s/(r)**0.5
                    ab =[cx-w/2,cy-h/2,cx+w/2,cy+h/2]
                    anchor.append(ab)
    return anchor 
                