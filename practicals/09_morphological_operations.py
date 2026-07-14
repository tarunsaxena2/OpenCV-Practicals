import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

# Apply Top Hat
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

# Apply Black Hat
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Top Hat", tophat)
cv2.imshow("Black Hat", blackhat)

# Save output
cv2.imwrite("outputs/tophat.jpg", tophat)
cv2.imwrite("outputs/blackhat.jpg", blackhat)

print("Morphology completed")

cv2.waitKey(0)
cv2.destroyAllWindows()