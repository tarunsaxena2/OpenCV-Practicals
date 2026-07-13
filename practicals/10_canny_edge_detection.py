import cv2
import os

# Read image
image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # Save output
    cv2.imwrite("outputs/canny_edges.jpg", edges)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", edges)

    print("Canny Edge Detection completed successfully.")
    print("Output saved in outputs/canny_edges.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()