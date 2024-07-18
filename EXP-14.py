import cv2
import numpy as np
import matplotlib.pyplot as plt
src_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype='float32')
dst_points = np.array([[0, 0], [2, 0], [2, 2], [0, 2]], dtype='float32') 
H, status = cv2.findHomography(src_points, dst_points)
print("Homography Matrix:\n", H)
image = np.zeros((100, 100, 3), dtype='uint8')
cv2.rectangle(image, (10, 10), (90, 90), (255, 255, 255), -1) 
pts = np.array([[10, 10], [90, 10], [90, 90], [10, 90]], dtype='float32')
pts_transformed = cv2.perspectiveTransform(pts[None, :, :], H)[0]
for pt in pts_transformed:
    cv2.circle(image, tuple(pt.astype(int)), 5, (0, 255, 0), -1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
