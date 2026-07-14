import cv2

# Open webcam
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if ret == False:
        break

    # Show webcam
    cv2.imshow("Webcam", frame)

    # Press q to close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

print("Webcam closed")