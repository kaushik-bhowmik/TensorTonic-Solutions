def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    res=[0 for i in range(256)]
    for row in range(len(image)):
        for col in range(len(image[0])):
            res[image[row][col]]+=1
    return res 