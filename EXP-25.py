import cv2
import numpy as np
import matplotlib.pyplot as plt
def sharpen_with_gradient_mask(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found or the path is incorrect")
    grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = cv2.magnitude(grad_x, grad_y)
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    gradient_magnitude = gradient_magnitude.astype(np.uint8)
    sharpened_img = cv2.add(img, gradient_magnitude)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image'), plt.axis('off')
    plt.subplot(1, 3, 2), plt.imshow(gradient_magnitude, cmap='gray'), plt.title('Gradient Magnitude'), plt.axis('off')
    plt.subplot(1, 3, 3), plt.imshow(sharpened_img, cmap='gray'), plt.title('Sharpened Image'), plt.axis('off')
    plt.show()
    return sharpened_img
image_path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png"
sharpened_image = sharpen_with_gradient_mask(image_path)
