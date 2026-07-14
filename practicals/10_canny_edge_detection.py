import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edge = cv2.Canny(gray, 100, 200)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Edges", edge)

# Save output
cv2.imwrite("outputs/canny.jpg", edge)

print("Edge detection done")

cv2.waitKey(0)
cv2.destroyAllWindows()