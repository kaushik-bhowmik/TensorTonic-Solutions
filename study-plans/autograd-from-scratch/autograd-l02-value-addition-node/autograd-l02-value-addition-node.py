import numpy as np

def value_addition_node(left, right, output_id):
    """
    Returns: an addition node that retains the two supplied leaf records as ordered parents
    """
    oval = left["data"] + right["data"]
    out = {"id":output_id, "data":oval, "grad":0.0, "op":"+","parents": [left, right]}
    return out 
