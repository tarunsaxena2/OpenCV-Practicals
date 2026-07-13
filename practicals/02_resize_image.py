import cv2
import os

image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    resized_image = cv2.resize(image, (500, 300))

    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite("outputs/resized_image.jpg", resized_image)

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized_image)

    print("Image resized successfully.")
    print("Resized image saved in outputs folder.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()