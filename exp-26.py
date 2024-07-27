import cv2
import numpy as np
image = cv2.imread(r"C:\Users\krish\OneDrive\Pictures\Screenshots\IMG-8,9,10,11,12.png")
watermark_text = "Watermark"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_color = (255, 255, 255)
font_thickness = 3
text_size, _ = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)
text_x = image.shape[1] - text_size[0] - 10
text_y = image.shape[0] - 10
overlay = image.copy()
cv2.putText(overlay, watermark_text, (text_x, text_y), font, font_scale, font_color, font_thickness)
alpha = 0.5
watermarked_image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
cv2.imwrite('watermarked_image.jpg', watermarked_image)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
