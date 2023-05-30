
#How to detect and draw contours around object in an image using OpenCV
#Libraries
import cv2
import sys
import numpy as np
from numba import cuda

#input image
input_image = cv2.imread("image_name")


#calling contours function
contours = find_contours(input_image)

#place contours over original input image
cv2.drawContours(input_image, contours, -1, (36,255,12), 2)

cv2.imshow("result with detected contour lines in pink", input_image)
cv2.waitkey(0)
cv2.destroyAllWindows()
