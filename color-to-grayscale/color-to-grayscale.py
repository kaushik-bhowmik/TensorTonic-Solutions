def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    res=[]
    for row in image:
        temp=[]
        for each in row:
            this= 0.299*each[0]+0.587*each[1]+0.114*each[2]
            temp.append(this)
        res.append(temp)
    return res 