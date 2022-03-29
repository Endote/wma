import linie_tray as lt
import kola_tray as kt
import cv2 as cv

img = cv.imread('tray7.jpg', cv.IMREAD_COLOR)
cimg = cv.imread('tray7.jpg', 0)
# gray = cv.imread('tray1.jpg', cv.IMREAD_GRAYSCALE)

def detect_coins_on_tray(tacka, kaska):
  result = []
  # print(kaska[0][0])
  for c in kaska[0]:
    if (c[0] <= tacka[0] and c[0] >= tacka[1]) and (c[1] <= tacka[2] and c[1] >= tacka[3]):
      result.append([c[0], c[1], c[2]])

  return result


if __name__ == '__main__':
  # cv.imshow('detected circles',cimg)

  lines = lt.get_lines(img)
  circles = kt.get_circles(cimg)

  # print(lines)
  # print(circles)

  tray = lt.get_maxes(lines)
  # print(tray)
  # coins = kt.get_circles_centers(circles)
  coins_on_tray = detect_coins_on_tray(tray, circles)
  
  print(coins_on_tray, sep='\n')
  
  lt.draw_lines(img, lines)
  kt.draw_circles(img, coins_on_tray)

  # print(str(len(coins_on_tray))+' <---Number of coins')
  cv.imshow(str(len(coins_on_tray))+' <---Number of coins',img)
  cv.waitKey(0)
  cv.destroyAllWindows()


