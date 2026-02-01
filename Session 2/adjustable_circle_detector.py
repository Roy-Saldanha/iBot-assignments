import os

import cv2
import numpy as np


def preprocess_image(image_path, blur_kernel=9):
    image = cv2.imread(image_path)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (blur_kernel, blur_kernel), 1)
    return blur


def detect_circles(gray_image, dp=1, minDist=50, param1=100, param2=30, minRadius=20, maxRadius=80):
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2,
                               minRadius=minRadius,
                               maxRadius=maxRadius)
    return circles


def visualize_circles(image, circles, save_path=None):
    original = image.copy()
    output = image.copy()

    if circles is not None:
        circles = circles.astype('uint16')
        for x, y, r in circles[0]:
            cv2.circle(output, (x, y), r, (0, 0, 0), 2)
            cv2.circle(output, (x, y), 2, (0, 0, 255), 3)

    if save_path is not None:
        cv2.imwrite(os.path.expanduser(save_path + '/sketch.jpg'), output)

    return np.hstack((original, output))


def print_statistics(circles):
    radii = np.transpose(circles[0])[2]
    print("The number of circles are", radii.shape[0])
    print("The smallest radius found in the set is", np.min(radii))
    print("The largest radius found in the set is", np.max(radii))
    print("The average radius in the set is", np.average(radii))


def dummy(x):
    pass


def run_with_trackbars(image, gray):
    cv2.namedWindow("Trackbars")

    cv2.createTrackbar("dp", "Trackbars", 1, 5, dummy)
    cv2.createTrackbar("minDist", "Trackbars", 50, 300, dummy)
    cv2.createTrackbar("param1", "Trackbars", 100, 300, dummy)
    cv2.createTrackbar("param2", "Trackbars", 30, 150, dummy)
    cv2.createTrackbar("minRadius", "Trackbars", 20, 200, dummy)
    cv2.createTrackbar("maxRadius", "Trackbars", 80, 300, dummy)

    while True:
        dp = cv2.getTrackbarPos("dp", "Trackbars")
        minDist = cv2.getTrackbarPos("minDist", "Trackbars")
        param1 = cv2.getTrackbarPos("param1", "Trackbars")
        param2 = cv2.getTrackbarPos("param2", "Trackbars")
        minRadius = cv2.getTrackbarPos("minRadius", "Trackbars")
        maxRadius = cv2.getTrackbarPos("maxRadius", "Trackbars")

        circles = detect_circles(
            gray,
            dp=dp,
            minDist=minDist,
            param1=param1,
            param2=param2,
            minRadius=minRadius,
            maxRadius=maxRadius
        )

        visualization = visualize_circles(image, circles)
        cv2.imshow("Original vs. Analysed", visualization)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    return circles


def main():
    path = 'test3.png'
    image = cv2.imread(path)
    circles = run_with_trackbars(image, preprocess_image(path))
    print_statistics(circles)


if __name__ == '__main__':
    main()
