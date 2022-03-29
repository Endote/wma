import linie_tray as lt
import kola_tray as kt
import cv2 as cv

def detect_coins_on_tray(tacka, kaska):
  result = []
  # print(kaska[0][0])
  for c in kaska[0]:
    if (c[0] <= tacka[0] and c[0] >= tacka[1]) and (c[1] <= tacka[2] and c[1] >= tacka[3]):
      result.append([c[0], c[1], c[2]])

  return result


if __name__ == '__main__':
  img = cv.imread('tray3.jpg', cv.IMREAD_COLOR)
  cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)

  lines = lt.get_lines(img)
  circles = kt.get_circles(img)

  tray = lt.get_maxes(lines)
  # coins = kt.get_circles_centers(circles)
  coins_on_tray = detect_coins_on_tray(tray, circles)

  print(coins_on_tray)
  
  img = lt.draw_lines(cimg, lines)
  img = kt.draw_circles(cimg, coins_on_tray)

  # print(coins)
  # print(circles)
  cv.imshow('detected circles',cimg)
  cv.waitKey(0)
  cv.destroyAllWindows()
  # print(kt.get_circles(img))
  # print(kt.get_circles_centers(circles))
  
  # p00 = [x_min, y_min]
  # p10 = [x_max, y_min]
  # p01 = [x_min, y_max]
  # p11 = [x_max, y_max]
  # tray = [x_max, x_min, y_max, y_min]
  # tray = [p00, p10, p01, p11]
  # print(detect_coins_on_tray(tray, coins))




