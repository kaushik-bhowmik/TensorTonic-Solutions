def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    tp = fp =fn=0
    classes = set(y_true)
    for c in classes:
        for i in range(len(y_true)):
            if y_true[i]==c and y_pred[i]==c:
                tp+=1
            elif y_true[i]!=c and y_pred[i]==c:
                fp+=1
            elif y_true[i]==c and y_pred[i]!=c:
                fn+=1 
    f1 = 2*tp/(2*tp+ fp +fn )
    return f1 
        