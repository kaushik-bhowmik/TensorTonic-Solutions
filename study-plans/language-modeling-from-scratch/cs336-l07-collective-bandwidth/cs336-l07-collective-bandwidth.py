def collective_bandwidth(payload_bytes: int, world_size: int, duration_seconds: float, collective: str) -> dict:
    """
    Returns a dict of floats: algorithm_bytes and bandwidth_bytes_per_second.
    """
    if collective=="all_reduce":
        c=2
    else:
        c = 1
    ab = c*payload_bytes *(world_size-1)/world_size
    B = ab/duration_seconds
    out = {"algorithm_bytes":ab,"bandwidth_bytes_per_second":B}
    return out 
