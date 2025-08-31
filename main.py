import cv2
import numpy as np

image = cv2.imread('input.jpg')
if image is None:
    print("ERROR OCCURRED")
    exit()


image = cv2.resize(image, (600, 500))

gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray_conversion, (5, 5), 0)


alpha = 1.8
beta = -0.8
gamma = 0
sharp = cv2.addWeighted(gray_conversion, alpha, blur, beta, gamma)


enhanced = cv2.equalizeHist(sharp)

combined = np.hstack((gray_conversion, enhanced))


cv2.imshow("Original vs Enhanced", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("output_image.jpg", enhanced)
