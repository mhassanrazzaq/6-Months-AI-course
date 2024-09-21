import numpy as np
import cv2 as cv

# read webcam using CV
# cap = cv.VideoCapture(0)

# if cap.isOpened():
#     ret, frame = cap.read()
#     print(ret)
#     print(frame)
# else:
#     ret = False
    
# while True:
#     ret, frame = cap.read()
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

#change the cam to greyscale cam 
cap = cv.VideoCapture(0)
# cap.set(6, 0.0) # 6 is the index of the property we
# # want to change, 0.0 is the value we want to set
# # it to
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

# convert color to black and white
# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     _, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
#     cv.imshow('frame', thresh)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()
