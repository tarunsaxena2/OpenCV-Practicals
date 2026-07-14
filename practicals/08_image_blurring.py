import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(img, (11, 11), 0)

# Apply Median Blur
median = cv2.medianBlur(img, 11)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)

# Save images
cv2.imwrite("outputs/gaussian.jpg", gaussian)
cv2.imwrite("outputs/median.jpg", median)

print("Blur completed")

cv2.waitKey(0)
cv2.destroyAllWindows()