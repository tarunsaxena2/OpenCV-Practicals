import cv2
import numpy as np

# Read image
img = cv2.imread("images/sample.jpg")

# Image size
rows, cols = img.shape[:2]

# Translation values
tx = 80
ty = 50

# Translation matrix
matrix = np.float32([[1, 0, tx],
                     [0, 1, ty]])

# Translate image
result = cv2.warpAffine(img, matrix, (cols, rows))

# Show images
cv2.imshow("Original", img)
cv2.imshow("Translated", result)

# Save image
cv2.imwrite("outputs/translated.jpg", result)

print("Translation done")

cv2.waitKey(0)
cv2.destroyAllWindows()