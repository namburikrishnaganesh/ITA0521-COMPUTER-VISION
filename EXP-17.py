import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
sobel_x_abs = np.absolute(sobel_x)
sobel_x_8u = np.uint8(sobel_x_abs)
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title('Sobel X Edge Detected Image')
plt.imshow(sobel_x_8u, cmap='gray')
plt.show()
