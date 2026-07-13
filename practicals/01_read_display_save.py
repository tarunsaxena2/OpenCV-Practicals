import cv2
import os

# Image path
image_path = "images/sample.jpg"

# Read image
image = cv2.imread(image_path)

# Check image
if image is None:
    print("Image not found. Please check the image path.")
else:
    # Display image
    cv2.imshow("Original Image", image)

    # Create output folder if it does not exist
    os.makedirs("outputs", exist_ok=True)

    # Save image
    output_path = "outputs/saved_image.jpg"
    cv2.imwrite(output_path, image)

    print("Image displayed successfully.")
    print("Image saved at:", output_path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()