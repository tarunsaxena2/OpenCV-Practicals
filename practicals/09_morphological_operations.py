import cv2
import os

# Read image
image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

    # Morphological operations
    top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # Save output images
    cv2.imwrite("outputs/top_hat.jpg", top_hat)
    cv2.imwrite("outputs/black_hat.jpg", black_hat)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Top Hat", top_hat)
    cv2.imshow("Black Hat", black_hat)

    print("Morphological operations completed successfully.")
    print("Top Hat image saved as outputs/top_hat.jpg")
    print("Black Hat image saved as outputs/black_hat.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()