import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Get image size
rows, cols = img.shape[:2]

# Rotate image by 45 degrees
matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

rotate_img = cv2.warpAffine(img, matrix, (cols, rows))

# Show images
cv2.imshow("Original", img)
cv2.imshow("Rotated", rotate_img)

# Save image
cv2.imwrite("outputs/rotated.jpg", rotate_img)

print("Rotation completed")

cv2.waitKey(0)
cv2.destroyAllWindows()