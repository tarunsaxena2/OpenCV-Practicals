import cv2

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open webcam.")
else:
    print("Webcam started successfully.")
    print("Press 'Q' to quit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Failed to capture frame.")
            break

        # Display webcam
        cv2.imshow("Webcam Capture", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

    print("Webcam closed successfully.")