import cv2
import numpy as np
image = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Could not load image.")
    exit()
kernel_size = (5, 5)
kernel = np.ones(kernel_size, np.uint8)
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite('dilation.png', dilation)
cv2.imshow('Dilated Image', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
