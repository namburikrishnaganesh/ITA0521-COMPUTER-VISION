import cv2
import numpy as np
image = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png")
if image is None:
    print("Error loading image.")
    exit()
kernel_size = (5, 5)
kernel = np.ones(kernel_size, np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=1)
dilated_image = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite('eroded_image.jpg', eroded_image)
cv2.imwrite('dilated_image.jpg', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
