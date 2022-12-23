import cv2
import numpy as np

# Setting frame size for webcam detection.
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def empty(a):
    pass

# Creating trackbars for threshold values for Cann edge detection
cv2.namedWindow('Parameters')
cv2.resizeWindow('Parameters', 640, 240)
cv2.createTrackbar('threshold1', 'Parameters', 255, 255, empty)
cv2.createTrackbar('threshold2', 'Parameters', 255, 255, empty)

# Creating a function for getting and drawing contours
def get_contours(img, img_contour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        sides = len(approx)

        if area > 1000 and sides == 7:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 255), 7)

# Converting to grayscale and making a mask object to detect red colour 
while True:
    success, vid = cap.read()
    imgContour = vid.copy()

    imgBlur = cv2.GaussianBlur(vid, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), 'uint8')

    # convert to hsv colorspace
    hsv = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)

    # lower bound and upper bound for red color
    lower_bound = np.array([136, 87, 111], np.uint8)
    upper_bound = np.array([180, 255, 255], np.uint8)

    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.dilate(mask, kernel)

    redOutput = cv2.bitwise_and(vid, vid, mask=mask)
    red_output = cv2.cvtColor(redOutput, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos('threshold1', 'Parameters')
    threshold2 = cv2.getTrackbarPos('threshold2', 'Parameters')
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    get_contours(red_output, imgContour)
    
    # Displaying the output.
    # cv2.imshow('Gray', imgGray)
    # cv2.imshow('Canny', imgCanny)
    # cv2.imshow('Diluted', imgDil)
    cv2.imshow('Contours', imgContour)
    # cv2.imshow('Vid', vid)
    cv2.imshow('Red Arrow', red_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
