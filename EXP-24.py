import cv2
import numpy as np
import matplotlib.pyplot as plt
def high_boost_filter(image_path, boost_factor=1.5):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found or the path is incorrect")
    blurred_img = cv2.GaussianBlur(img, (7, 7), 0)
    mask = cv2.subtract(img, blurred_img)
    high_boost_mask = cv2.multiply(mask, boost_factor)
    sharpened_img = cv2.add(img, high_boost_mask)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image'), plt.axis('off')
    plt.subplot(1, 3, 2), plt.imshow(blurred_img, cmap='gray'), plt.title('Blurred Image'), plt.axis('off')
    plt.subplot(1, 3, 3), plt.imshow(sharpened_img, cmap='gray'), plt.title('High-Boost Sharpened Image'), plt.axis('off')
    plt.show()
    return sharpened_img
image_path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png"
high_boost_image = high_boost_filter(image_path, boost_factor=1.5)
