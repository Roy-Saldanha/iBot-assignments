import cv2
import numpy as np


def preprocess_image(image, blur_kernel=9):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (blur_kernel, blur_kernel), 1)
    return blur


def detect_circles(gray_image, dp=1, minDist=50, param1=100, param2=30, minRadius=20, maxRadius=80):
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2,
                               minRadius=minRadius,
                               maxRadius=maxRadius)
    return circles


def visualize_circles(image, circles):
    original = image.copy()
    output = image.copy()

    if circles is not None:
        circles = circles.astype('uint16')
        for x, y, r in circles[0]:
            cv2.circle(output, (x, y), r, (0, 0, 0), 2)
            cv2.circle(output, (x, y), 2, (0, 0, 255), 3)

    return np.hstack((original, output))


def dummy(x):
    pass


def create_trackbars():
    cv2.namedWindow("Trackbars")

    cv2.createTrackbar("dp", "Trackbars", 1, 5, dummy)
    cv2.createTrackbar("minDist", "Trackbars", 50, 300, dummy)
    cv2.createTrackbar("param1", "Trackbars", 100, 300, dummy)
    cv2.createTrackbar("param2", "Trackbars", 30, 150, dummy)
    cv2.createTrackbar("minRadius", "Trackbars", 20, 200, dummy)
    cv2.createTrackbar("maxRadius", "Trackbars", 80, 300, dummy)


def capture():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Live circle detector")
    if not cap.isOpened():
        print("Camera not opening")
        exit()

    create_trackbars()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        gray = preprocess_image(frame)

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

        cv2.imshow("Live circle sketch", visualize_circles(frame, circles))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    capture()


if __name__ == '__main__':
    main()
