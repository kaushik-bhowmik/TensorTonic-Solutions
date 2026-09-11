def rating_normalization(matrix: list) -> list:
    """
    Returns the mean-centered user-item matrix.
    """
    # Write code here
    users = [0 for each in range(len(matrix))]
    for i,each  in enumerate(matrix):
        #mean = sum(each)/len(each)
        count=0 ; tot=0
        for j in range(len(each)):
            if each[j]!=0:
                count+=1
                tot+=each[j]
        if count==0:
            pass
        else: 
            mean = tot/count 
            users[i] = mean 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]!=0:
                matrix[i][j]-=users[i]
    return matrix 
        