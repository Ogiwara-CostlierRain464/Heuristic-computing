import os
import sys

import cv2

if len(sys.argv) < 2:
    print("enter figure name")
    sys.exit()


def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("face_cv2.xml")
    rects = cascade.detectMultiScale(img, 1.0342, 6, cv2.CASCADE_SCALE_IMAGE, (20, 20))
    #    rects = cascade.detectMultiScale(img,1.0342,6,cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img


def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)


path = str(sys.argv[1])
rects, img = detect(path)
image = cv2.imread(path)
box(rects, img)
cv2.putText(img, str(len(rects)), (80, 80), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0), 3)
print(len(rects))
image = cv2.resize(image, (int(image.shape[1] / 2), int(image.shape[0] / 2)))
img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow('input', image)
cv2.imshow('result', img)
cv2.imwrite('detected.jpg', img)
k = cv2.waitKey(0)
if cv2.waitKey(300) == 27:
    cv2.destroyAllWindows()
    os._exit(0)
