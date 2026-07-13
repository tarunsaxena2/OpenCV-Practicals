import cv2
import os

image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    horizontal_flip = cv2.flip(image, 1)
    vertical_flip = cv2.flip(image, 0)
    both_flip = cv2.flip(image, -1)

    os.makedirs("outputs", exist_ok=True)

    cv2.imwrite("outputs/horizontal_flip.jpg", horizontal_flip)
    cv2.imwrite("outputs/vertical_flip.jpg", vertical_flip)
    cv2.imwrite("outputs/both_flip.jpg", both_flip)

    cv2.imshow("Original Image", image)
    cv2.imshow("Horizontal Flip", horizontal_flip)
    cv2.imshow("Vertical Flip", vertical_flip)
    cv2.imshow("Both Flip", both_flip)

    print("Image flipping completed successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()