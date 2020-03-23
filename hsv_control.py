import cv2
import numpy as np

img = cv2.imread(r'/home/siddharth/Documents/abhiyaan_trial/1.png',1)
# cv2.imshow('fheuf', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow("image")
def nothing(x):
    pass
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
    mask = cv2.inRange(hsv, low_limit, up_limit)
    res = cv2.bitwise_and(img,img,mask = mask)
    cv2.imshow("imag",res)
    cv2.imshow("mask",mask)
  
cv2.destroyAllWindows()