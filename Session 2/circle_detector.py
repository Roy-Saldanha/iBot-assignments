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
    if circles is not None:
        circles = circles.astype('uint16')
        for x, y, r in circles[0]:
            cv2.circle(image, (x, y), r, (0, 0, 0), 2)
            cv2.circle(image, (x, y), 2, (0, 0, 255), 3)
    else:
        print("No valid circles recognized")
    if save_path is not None:
        cv2.imwrite(os.path.expanduser(save_path + '/sketch.jpg'), image)
    return np.hstack((original, image))


def print_statistics(circles):
    radii = np.transpose(circles[0])[2]
    print("The number of circles are", radii.shape[0])
    print("The smallest radius found in the set is", np.min(radii))
    print("The largest radius found in the set is", np.max(radii))
    print("The average radius in the set is", np.average(radii))


def save_statistics(circles, save_path=None):
    radii = np.transpose(circles[0])[2]
    if save_path is not None:
        with open(save_path + '/output.txt', "w") as f:
            f.write(
                f"The number of circles are {radii.shape[0]}\nThe smallest radius found in the set is {np.min(radii)}\nThe largest radius found in the set is {np.max(radii)}\nThe average radius in the set is {np.average(radii)}")


def main():
    path = 'test3.png'
    image = cv2.imread(path)
    circles = detect_circles(preprocess_image(path))
    visualization = visualize_circles(image, circles, '/Users/saldanha.roy/Desktop')
    cv2.imshow("Original vs. Analysed", visualization)
    cv2.waitKey(0)
    print_statistics(circles)


if __name__ == '__main__':
    main()
