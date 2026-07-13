import cv2
import os

image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    output = image.copy()

    # Draw a line
    cv2.line(output, (50, 50), (300, 50), (255, 0, 0), 4)

    # Draw a rectangle
    cv2.rectangle(output, (50, 100), (300, 250), (0, 255, 0), 4)

    # Draw a circle
    cv2.circle(output, (450, 170), 70, (0, 0, 255), 4)

    # Add text
    cv2.putText(
        output,
        "OpenCV Practical",
        (50, 320),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite("outputs/shapes_and_text.jpg", output)

    cv2.imshow("Original Image", image)
    cv2.imshow("Shapes and Text", output)

    print("Shapes and text added successfully.")
    print("Output saved in outputs/shapes_and_text.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()