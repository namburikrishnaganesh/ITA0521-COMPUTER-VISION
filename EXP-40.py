import cv2
img = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-39.jpeg")
x, y = 100, 100
width, height = 200, 150
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows() 
