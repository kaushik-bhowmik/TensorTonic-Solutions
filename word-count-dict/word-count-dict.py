def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    pass
    print(sentences)
    rec= {}
    for each in sentences:
        for token in each:
            rec[token] = rec.get(token, 0) + 1
    return rec    