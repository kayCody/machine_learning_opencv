import cv2 as cv
import sys
#kwameis a good hacker a systems engineer...cv perod
image = cv.imread(cv.samples.findFile("/Users/apple/Downloads/IMG_4936.jpg"))

if image is None:
    sys.exit("could not load image")
else:
    cv.imshow("Display window", image)
    k = cv.waitKey(0)

    if k == ord("s"):
        cv.imwrite("new_image.jpg", image)
