import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Resize image
resize = cv2.resize(img, (500, 300))

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resize)

# Save resized image
cv2.imwrite("outputs/resized_image.jpg", resize)

print("Resize completed")

cv2.waitKey(0)
cv2.destroyAllWindows()