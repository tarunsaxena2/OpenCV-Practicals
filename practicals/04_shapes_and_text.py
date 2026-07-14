import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Copy image
new_img = img.copy()

# Draw line
cv2.line(new_img, (40, 40), (250, 40), (255, 0, 0), 3)

# Draw rectangle
cv2.rectangle(new_img, (50, 80), (250, 220), (0, 255, 0), 3)

# Draw circle
cv2.circle(new_img, (400, 150), 50, (0, 0, 255), 3)

# Add text
cv2.putText(new_img, "Tarun Saxena", (50, 300),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Output", new_img)

# Save image
cv2.imwrite("outputs/shapes_text.jpg", new_img)

print("Shapes added")

cv2.waitKey(0)
cv2.destroyAllWindows()