import cv2
import numpy as np

def capture():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Live Pencil Sketch")
    cv2.createTrackbar("Blur", "Live Pencil Sketch", 21, 99, dummy)
    if not cap.isOpened():
        print("Camera not opening")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        blur_val = cv2.getTrackbarPos("Blur", "Live Pencil Sketch")
        if blur_val < 1:
            blur_val = 1
        if blur_val % 2 == 0:
            blur_val += 1
        cv2.imshow("Live Pencil Sketch", video_sketch(frame,blur_val))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def video_sketch(original, blur_kernel):
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    inverted = 255 - grayscale
    inverted_blur = cv2.GaussianBlur(inverted, (blur_kernel, blur_kernel), 0)
    blur = 255 - inverted_blur
    sketch = np.minimum(255, 256 * (grayscale / (1e-6 + blur)))
    sketch = sketch.astype(np.uint8)
    sketch=cv2.cvtColor(sketch,cv2.COLOR_GRAY2BGR)
    combined = np.hstack((original, sketch))
    return combined

def dummy(x):
    pass


def main():
    capture()
main()