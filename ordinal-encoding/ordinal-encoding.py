from collections import defaultdict
def ordinal_encoding(values: list, ordering: list) -> list:
    """
    Returns the ordinal index of every input value.
    """
    # Write code here
    rec = defaultdict(int) ; ans =[]
    for i, each in enumerate(ordering):
        rec[each]=i
    for each in values:
        ans.append(rec[each])
    return ans 