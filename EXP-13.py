import cv2
import numpy as np
def perspective_transformation(frame, src_points, dst_points):
    M = cv2.getPerspectiveTransform(np.float32(src_points), np.float32(dst_points))
    (h, w) = frame.shape[:2]
    transformed_frame = cv2.warpPerspective(frame, M, (w, h))
    return transformed_frame
src_points = np.float32([[100, 100], [500, 100], [100, 400], [500, 400]])
dst_points = np.float32([[200, 150], [400, 150], [200, 350], [400, 350]])
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        transformed_frame = perspective_transformation(frame, src_points, dst_points)
        cv2.imshow('Transformed Video', transformed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
