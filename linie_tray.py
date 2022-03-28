import cv2 as cv
import numpy as np
img = cv.imread('tray3.jpg', cv.IMREAD_COLOR)  
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Gaussian blur from the internet

# https://stackoverflow.com/questions/66569066/how-do-i-optimize-line-detection-for-different-images


blur = cv.GaussianBlur(gray,(5,5),20)

edges = cv.Canny(gray,1,5000,apertureSize = 5)
#lines = cv.HoughLinesP(edges,rho = 1, theta = 1*np.pi/180,treshold = 100, minLineLength=50, maxLineGap=6.5)
lines = cv.HoughLinesP(edges,rho = 1, theta = 1*np.pi/180, threshold = 120,  maxLineGap=400)

print(lines.shape)
for line in lines:
    print(line)
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv.imshow("Linie", img)
k = cv.waitKey(0)
