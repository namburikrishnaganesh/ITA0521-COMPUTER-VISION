import cv2
import numpy as np
def affine_transformation(image, src_points, dst_points):
    M = cv2.getAffineTransform(np.float32(src_points), np.float32(dst_points))
    (h, w) = image.shape[:2]
    transformed_image = cv2.warpAffine(image, M, (w, h))
    return transformed_image
image_path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png"
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
else:
    src_points = np.float32([[50, 50], [200, 50], [50, 200]])
    dst_points = np.float32([[10, 100], [200, 50], [100, 250]])
    transformed_image = affine_transformation(image, src_points, dst_points)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
