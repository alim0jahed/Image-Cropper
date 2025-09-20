from email.mime import image

import cv2 as cv
import argparse


ref_points = []
crop = False

def shape_selection(event, x, y, flags, param):
    global ref_points, crop
    if event == cv.EVENT_LBUTTONDOWN:
        ref_points=[(x, y)]

    elif event == cv.EVENT_LBUTTONUP:
        ref_points.append((x, y))
        cv.rectangle(image, ref_points[0], ref_points[1], (0, 255, 0), 2)
        cv.imshow("Image", image)

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv.imread(args['image'])
clone = image.copy()
cv.namedWindow('image')
cv.setMouseCallback('image', shape_selection)

while True:
    cv.imshow('image', image)
    key = cv.waitKey(1) & 0xFF

    if key == ord('r'):
        image = clone.copy()
    elif key == ord('c'):
        break
if len(ref_points) == 2:
    cropped_image = clone[ref_points[0][1]:ref_points[1][1], ref_points[0][0]:ref_points[1][0]]
    cv.imshow('cropped image', cropped_image)
    cv.waitKey(0)

cv.destroyAllWindows()