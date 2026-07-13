import cv2
import os

input_path = "videos/sample_video.mp4"
output_path = "outputs/output_video.mp4"

# Open input video
video = cv2.VideoCapture(input_path)

if not video.isOpened():
    print("Video file not found or could not be opened.")
else:
    os.makedirs("outputs", exist_ok=True)

    # Get video properties
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Use default FPS if FPS is unavailable
    if fps <= 0:
        fps = 25

    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    while True:
        success, frame = video.read()

        if not success:
            break

        # Write frame to output video
        writer.write(frame)

        # Display video
        cv2.imshow("Video Read and Write", frame)

        # Press Q to stop video
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    video.release()
    writer.release()
    cv2.destroyAllWindows()

    print("Video reading and writing completed successfully.")
    print("Output saved in:", output_path)