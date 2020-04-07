from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
from time import sleep

temp1=1

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

# (hMin = 0 , sMin = 126, vMin = 152), (hMax = 37 , sMax = 255, vMax = 255)
LowerBound = np.array([20,65,226])
UpperBound = np.array([45,242,255])
#yellow color
#LowerBound = np.array([20, 100, 100])
#UpperBound = np.array([30, 255, 255])
#orange color
#LowerBound = np.array([20, 100, 100])
#UpperBound = np.array([30, 255, 255])
pts = deque(maxlen=args["buffer"])

# vs = cv2.VideoCapture("/home/lordgrim/cricket-bot-cv/ball-tracking/ball_tracking_example.mp4")
vs = cv2.VideoCapture('landing_recording_Trim.mp4')

# allow the camera or video file to warm up
time.sleep(2.0)
radius = 0

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# keep looping
while True:
    a = time.time()
    # grab the current frame
    ret, frame = vs.read()
    if frame is None:
        break
    frame75 = rescale_frame(frame, percent=75)

    # resize the frame, blur it, and convert it to the HSV
    # color space

    blurred = cv2.GaussianBlur(frame75, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Mask and cleanup
    mask = cv2.inRange(hsv, LowerBound, UpperBound)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('mask', mask)
    # find contours in the mask and initialize the current
    # (x, y) center of the landing pad
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 5:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame75, (int(x), int(y)), int(radius),
                (0, 0, 255), 2)
            cv2.circle(frame75, center, 5, (0, 255, 0), -1)
            print('radius: ',radius, ';x-coord: ',int(x),';y-coord: ',int(y))


    # show the frame to our screen
    cv2.imshow("frame75", frame75)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

vs.release()

# close all windows
cv2.destroyAllWindows()
