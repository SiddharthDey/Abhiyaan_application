import cv2
import numpy as np

img = cv2.imread(r'/home/siddharth/Documents/abhiyaan_trial/1.png',1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low_green = np.array([36, 0, 0])
up_green = np.array([86, 255, 255])
mask_green = cv2.inRange(hsv, low_green, up_green)

low_red = np.array([0, 100, 100])
up_red = np.array([10, 255, 255])
mask_red = cv2.inRange(hsv, low_red, up_red)

low_yellow = np.array([20, 100, 100])
up_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv, low_yellow, up_yellow)

count_green = 0
count_red = 0
count_yellow = 0
for i in range(0,hsv.shape[0]):
    for j in range(0,hsv.shape[1]):
        if mask_green[i][j]==255:
            count_green = count_green + 1
        if mask_red[i][j]==255:
            count_red = count_red + 1
        if mask_yellow[i][j]==255:
            count_yellow = count_yellow + 1

if count_green>1000:
    print("green light")
if count_red>1000:
    print("red light")
if count_yellow>1000:
    print("yellow light")

