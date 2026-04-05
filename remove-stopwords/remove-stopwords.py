def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    pass
    swl = set(stopwords) ; res=[]
    for each in tokens:
        if each not in swl:
            res.append(each)
    return res