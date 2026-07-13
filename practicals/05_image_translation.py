import cv2
import numpy as np
import os

# Read image
image = cv2.imread("images/sample.jpg")

if image is None:
    print("Image not found.")
else:
    rows, cols = image.shape[:2]

    # Translation Matrix
    tx = 100  # Shift right
    ty = 50   # Shift down

    translation_matrix = np.float32([
        [1, 0, tx],
        [0, 1, ty]
    ])

    translated = cv2.warpAffine(image, translation_matrix, (cols, rows))

    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite("outputs/translated_image.jpg", translated)

    cv2.imshow("Original Image", image)
    cv2.imshow("Translated Image", translated)

    print("Image translated successfully.")
    print("Output saved in outputs/translated_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()