import cv2
import numpy as np 
img = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png", cv2.IMREAD_GRAYSCALE) 
kernel = np.ones((5,5), np.uint8) 
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", grad)
cv2.waitKey 
