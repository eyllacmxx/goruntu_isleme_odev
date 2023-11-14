# import the necessary packages
import numpy as np
import cv2

# load the image
image = cv2.imread("download.jpg")

# define the list of boundaries

boundaries = [
    ([17, 10, 100], [50, 60, 200]),
    ([25, 146, 190], [100, 180, 250])]

for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("images", output)
    cv2.waitKey(0)