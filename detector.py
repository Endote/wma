import linie_tray as lt
import kola_tray as kt
import cv2 as cv



if __name__ == '__main__':
    img = cv.imread('tray3.jpg', cv.IMREAD_COLOR)
    lines = lt.get_lines(img)
    img = lt.draw_lines(img, lines) 
    print(lines) 
