#The following code has been written to mask the given image by limiting the upper and lower hsv values to get the
#the desired part of the image by creating trackbars to control the upper and lower limits

import cv2
import numpy as np

img = cv2.imread(r'/home/siddharth/Documents/abhiyaan_trial/lanes.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow("image")
def nothing(x):
    pass
#creating trackbars to limit the upper and lower and hsv values
cv2.createTrackbar('Hmin','image',0,180,nothing)
cv2.createTrackbar('Hmax','image',180,180,nothing)
cv2.createTrackbar('Smin','image',0,255,nothing)
cv2.createTrackbar('Smax','image',255,255,nothing)
cv2.createTrackbar('Vmin','image',0,255,nothing)
cv2.createTrackbar('Vmax','image',255,255,nothing)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    h_min = cv2.getTrackbarPos('Hmin','image')
    h_max = cv2.getTrackbarPos('Hmax','image')
    s_min = cv2.getTrackbarPos('Smin','image')
    s_max = cv2.getTrackbarPos('Smax','image')
    v_min = cv2.getTrackbarPos('Vmin','image')
    v_max = cv2.getTrackbarPos('Vmax','image')
    print("h_min:",h_min,"s_min:",s_min,"v_min:",v_min,"\n")
    print("h_max:",h_max,"s_max:",s_max,"v_max:",v_max,"\n")
    low_limit = np.array([h_min, s_min, v_min])
    up_limit = np.array([h_max, s_max, v_max])
    #putting a mask on the original image getting only two values,255 if lying within the given range or 0
    mask = cv2.inRange(hsv, low_limit, up_limit)
    #bitwise addition of the pixel values of the mask and the original image
    res = cv2.bitwise_and(img,img,mask = mask)
    cv2.imshow("imag",res)
    cv2.imshow("mask",mask)
  
cv2.destroyAllWindows()