import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Flip image
flip1 = cv2.flip(img, 1)
flip2 = cv2.flip(img, 0)
flip3 = cv2.flip(img, -1)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Horizontal Flip", flip1)
cv2.imshow("Vertical Flip", flip2)
cv2.imshow("Both Flip", flip3)

# Save images
cv2.imwrite("outputs/horizontal.jpg", flip1)
cv2.imwrite("outputs/vertical.jpg", flip2)
cv2.imwrite("outputs/both.jpg", flip3)

print("Image flipped")

cv2.waitKey(0)
cv2.destroyAllWindows()