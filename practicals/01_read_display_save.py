import cv2

# image ko read karna
img = cv2.imread("images/sample.jpg")

# image ko display karna
cv2.imshow("My Image", img)

# image ki copy save karna
cv2.imwrite("outputs/saved_image.jpg", img)

print("Image saved successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()