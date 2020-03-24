import cv2
import numpy as np

img = cv2.imread(r'/home/siddharth/Desktop/lanes.jpg',1)
#pre-processing the image by applying Gaussian filter
img1 = cv2.GaussianBlur(img, (5, 5), 0)
#converting the rgb values to hsv
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#the hsv upper and lower limits for detecting yellow lanes has obtained using the hsv_control.py code present in the repository  
low_yellow = np.array([18, 94, 140])
up_yellow = np.array([48, 255, 255])
mask1 = cv2.inRange(hsv, low_yellow, up_yellow)
#canny edge detection to get the coordinates of all the edges
edges1 = cv2.Canny(mask1, 75, 150)
#using Hough line transformation to detect straight edges from all the canny edges detected
lines1 = cv2.HoughLinesP(edges1, 1, np.pi/180, 50, maxLineGap=50)

#the hsv upper and lower limits for detecting white lanes has obtained using the hsv_control.py code present in the repository
low_white = np.array([81, 0, 177])
up_white = np.array([128, 22, 255])
mask2 = cv2.inRange(hsv, low_white, up_white)
edges2 = cv2.Canny(mask2, 75, 150)
lines2 = cv2.HoughLinesP(edges2, 1, np.pi/180, 50, maxLineGap=200)

#drawing straight lines on the straught edges detected using cv2.line() function
if lines1 is not None:
    for line1 in lines1:
        x1, y1, x2, y2 = line1[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

if lines2 is not None:
    for line2 in lines2:
        x1, y1, x2, y2 = line2[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5) 

cv2.imshow("img1",img)
cv2.waitKey(0)