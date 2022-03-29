from cmath import inf
import cv2 as cv
import numpy as np




# Gaussian blur from the internet

# https://stackoverflow.com/questions/66569066/how-do-i-optimize-line-detection-for-different-images




def get_maxes(lines):
    x_max = -float(inf)
    x_min = float(inf)
    y_max = -float(inf)
    y_min = float(inf)
    for line in lines:
        # print(line)
        x1,y1,x2,y2 = line[0]
        if(x1 > x_max or x2 > x_max):
            if(x1 > x2):
                x_max = int(x1)
            else:
                x_max = int(x2)
        if(x1 < x_min or x2 < x_min):
            if(x1 < x2):
                x_min = int(x1)
            else:
                x_min = int(x2)
        if(y1 > y_max or y2 > y_max):
            if(y1 > y2):
                y_max = int(y1)
            else:
                y_max = int(y2)
        if(y1 < y_min or y2 < y_min):
            if(y1 < y2):
                y_min = int(y1)
            else:
                y_min = int(y2)

    return [x_max, x_min, y_max, y_min]


def get_lines(obraz):
    
    gray = cv.cvtColor(obraz,cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(gray,(5,5),2)

    edges = cv.Canny(gray,1,5000,apertureSize = 5)
#lies = cv.HoughLinesP(edges,rho = 1, theta = 1*np.pi/180,treshold = 100, minLineLength=50, maxLineGap=6.5)
    return cv.HoughLinesP(edges,rho = 1, theta = 1*np.pi/180, threshold = 150,  maxLineGap=150)

def draw_lines(obraz, lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        obraz = cv.line(obraz,(x1,y1),(x2,y2),(0,255,0),2)
    return obraz



# if __name__ == '__main__':
    # img = cv.imread('tray3.jpg', cv.IMREAD_COLOR)  

    # lines = get_lines(img)


    # x_max, x_min, y_max, y_min = get_maxes(lines)


    # for line in lines:
    #     print(line)
    #     x1,y1,x2,y2 = line[0]
    #     if(x1 > x_max or x2 > x_max):
    #         if(x1 > x2):
    #             x_max = int(x1)
    #         else:
    #             x_max = int(x2)

    #     if(x1 < x_min or x2 < x_min):
    #         if(x1 < x2):
    #             x_min = int(x1)
    #         else:
    #             x_min = int(x2)


    #     if(y1 > y_max or y2 > y_max):
    #         if(y1 > y2):
    #             y_max = int(y1)
    #         else:
    #             y_max = int(y2)

    #     if(y1 < y_min or y2 < y_min):
    #         if(y1 < y2):
    #             y_min = int(y1)
    #         else:
    #             y_min = int(y2)
    


    #     cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # draw_lines(img, lines)
    # cv.imshow("Linie", img)
    # # print(str(x_max)+' '+str(x_min))
    # print(get_maxes(lines))
    # k = cv.waitKey(0)




