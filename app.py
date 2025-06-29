import cv2

image = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = cv2.bitwise_not(gray)
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = cv2.bitwise_not(blurred)
sketch = cv2.divide(gray, inverted_blur, scale=256.0)

cv2.imwrite("sketch.png", sketch)
cv2.imshow("Pencil Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
