import cv2
img = cv2.imread("sample1.jpg")
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
#dst=cv2.GaussianBlur(src,(kernel),borderType)
cv2.imwrite("gaussianImage.jpg",gaussianBlurImg)
