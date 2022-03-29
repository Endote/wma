import numpy as np
import cv2 as cv

# https://stackoverflow.com/questions/10716464/what-are-the-correct-usage-parameter-values-for-houghcircles-in-opencv-for-iris

img = cv.imread('tray7.jpg',0)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)

def get_circles(obraz):

    obraz = cv.medianBlur(obraz, 3)
    circles = cv.HoughCircles(obraz, cv.HOUGH_GRADIENT,1,20,param1=60,param2=40,minRadius=0,maxRadius=120)
    circles = np.uint16(np.around(circles))
    return circles


def get_circles_centers(circles):
    centers = []
    for i in circles[0,:]:
    # draw the outer circle
        # cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
        # cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        centers.append([int(i[0]),int(i[1])])
    return centers

def draw_circles(cimg, circles):
    # print(circles)
    for i in circles:
        print(i)
    # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


if __name__ == '__main__':
    # circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20, param1=60,param2=40,minRadius=0,maxRadius=120)
    circles = get_circles(img)

    circles = np.uint16(np.around(circles))

    draw_circles(cimg, circles[0])
    # print(circles[0])
    cv.imshow('detected circles',cimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
