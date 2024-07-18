import cv2
import numpy as np
def perspective_transformation(image, src_points, dst_points):
    M = cv2.getPerspectiveTransform(np.float32(src_points), np.float32(dst_points))
    (h, w) = image.shape[:2]
    transformed_image = cv2.warpPerspective(image, M, (w, h))
    return transformed_image
image_path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png"
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
else:
    src_points = np.float32([[100, 100], [200, 100], [100, 200], [200, 200]])
    dst_points = np.float32([[50, 150], [250, 150], [50, 300], [250, 300]])
    transformed_image = perspective_transformation(image, src_points, dst_points)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
