import cv2
import os

# Read image
image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    # Apply Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(image, (11, 11), 0)

    # Apply Median Blur
    median_blur = cv2.medianBlur(image, 11)

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # Save output images
    cv2.imwrite("outputs/gaussian_blur.jpg", gaussian_blur)
    cv2.imwrite("outputs/median_blur.jpg", median_blur)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur", gaussian_blur)
    cv2.imshow("Median Blur", median_blur)

    print("Image blurring completed successfully.")
    print("Gaussian Blur saved as outputs/gaussian_blur.jpg")
    print("Median Blur saved as outputs/median_blur.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()