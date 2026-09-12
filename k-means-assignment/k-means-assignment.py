def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    res =[]
    for i, point in enumerate(points):
        cluster= -1 ; dist = float("inf")
        for j, centroid in enumerate(centroids):
            distance = 0
            for d in range(len(point)):
                distance += (point[d] - centroid[d]) ** 2
            if dist>distance:
                cluster = j
                dist = distance 
        res.append(cluster)
    return res 
        