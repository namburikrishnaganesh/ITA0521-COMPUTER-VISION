import cv2
def display_video(speed=1):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('Webcam Video', frame)
        delay = int(1000 / (30 * speed))
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
print("Press 'q' to exit the video window.")
print("Displaying video in normal speed...")
display_video(speed=1)
print("Displaying video in slow motion (0.5x speed)...")
display_video(speed=0.5)
print("Displaying video in fast motion (2x speed)...")
display_video(speed=2)
