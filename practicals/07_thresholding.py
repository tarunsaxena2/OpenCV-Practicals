import cv2
import os

# Read image
image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary threshold
    threshold_value, binary_image = cv2.threshold(
        gray_image,
        127,
        255,
        cv2.THRESH_BINARY
    )

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # Save output
    cv2.imwrite("outputs/binary_threshold.jpg", binary_image)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("Binary Threshold", binary_image)

    print("Binary thresholding completed successfully.")
    print("Threshold value:", threshold_value)
    print("Output saved in outputs/binary_threshold.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()