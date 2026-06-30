def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here'
    
    res =[] ; st =0
    while st<len(tokens):
        end = min(len(tokens),st+chunk_size)
        res.append(tokens[st:end])
        st = st+chunk_size-overlap 
        if end == len(tokens):
            break
    return res 