import cv2
path = r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
