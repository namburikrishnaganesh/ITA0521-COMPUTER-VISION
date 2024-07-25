import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.convertScaleAbs(sobel_y)
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title('Sobel Y Edge Detection')
plt.imshow(sobel_y, cmap='gray')
plt.show()
