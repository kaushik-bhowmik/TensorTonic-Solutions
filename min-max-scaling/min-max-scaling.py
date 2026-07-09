def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    min_max=[] ; res=[]
    for col in range(len(data[0])):
        mini = float("inf")
        maxi = float("-inf")
        for row in range(len(data)):
            mini = min(mini, data[row][col])
            maxi = max(maxi, data[row][col])
        min_max.append([mini,maxi])
    for row in range(len(data)):
        this_row =[]
        for col in range(len(data[0])):
            if min_max[col][1]- min_max[col][0]!=0:
                this_row.append((data[row][col]-min_max[col][0])/(min_max[col][1]- min_max[col][0]))
            else:
                this_row.append(0)
        res.append(this_row)
    return res 