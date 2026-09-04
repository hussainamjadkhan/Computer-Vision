pip install opencv-python

import cv2
image = cv2.imread("example.jpg")
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
