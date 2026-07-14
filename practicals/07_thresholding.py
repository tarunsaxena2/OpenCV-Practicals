import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Gray Image", gray)
cv2.imshow("Binary Image", binary)

# Save output
cv2.imwrite("outputs/binary.jpg", binary)

print("Threshold applied")

cv2.waitKey(0)
cv2.destroyAllWindows()