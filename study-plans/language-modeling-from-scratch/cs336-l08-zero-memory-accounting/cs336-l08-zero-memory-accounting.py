from math import ceil 
def zero_memory_accounting(parameter_bytes: int, gradient_bytes: int, optimizer_bytes: int, world_size: int) -> dict:
    """
    Returns a dict of integer byte counts: ddp, zero1, zero2, zero3.
    """
    ddp = parameter_bytes +gradient_bytes + optimizer_bytes
    mz1 = parameter_bytes + gradient_bytes + ceil(optimizer_bytes/world_size)
    mz2 = parameter_bytes + ceil((optimizer_bytes+gradient_bytes)/world_size)
    mz3 = ceil((parameter_bytes+optimizer_bytes+gradient_bytes)/world_size)
    return {"ddp":ddp, "zero1":mz1, "zero2":mz2,"zero3":mz3}
    
