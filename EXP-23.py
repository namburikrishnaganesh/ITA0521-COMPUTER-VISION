import cv2
import numpy as np
img = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]) 
laplacian = cv2.filter2D(gray, -1, laplacian_kernel)
sharpened = cv2.add(gray, laplacian)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows() 
