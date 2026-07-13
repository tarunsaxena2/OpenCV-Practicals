import cv2
import os

# Read image
image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    rows, cols = image.shape[:2]

    # Rotation Matrix (45 degrees)
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)

    # Rotate Image
    rotated = cv2.warpAffine(image, rotation_matrix, (cols, rows))

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # Save rotated image
    cv2.imwrite("outputs/rotated_image.jpg", rotated)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated)

    print("Image rotated successfully.")
    print("Output saved in outputs/rotated_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()