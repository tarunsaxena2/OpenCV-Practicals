import cv2

# Open video
video = cv2.VideoCapture("videos/sample_video.mp4")

# Get video size
width = int(video.get(3))
height = int(video.get(4))
fps = 20

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("outputs/output_video.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = video.read()

    if ret == False:
        break

    # Show video
    cv2.imshow("Video", frame)

    # Save video
    out.write(frame)

    # Press q to stop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

print("Video completed")