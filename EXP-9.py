import cv2
import numpy as np
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated
image_path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png"
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
else:
    rotated_clockwise = rotate_image(image, -90)
    rotated_counterclockwise = rotate_image(image, 90)
    cv2.imshow("Rotated Clockwise", rotated_clockwise)
    cv2.imshow("Rotated Counter-Clockwise", rotated_counterclockwise)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
