import cv2
import numpy as np
import os


def pencil_sketch(image_path, blur_kernel=25):
    original = cv2.imread(image_path)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    inverted = 255 - grayscale
    inverted_blur = cv2.GaussianBlur(inverted, (blur_kernel, blur_kernel), 0)
    blur = 255 - inverted_blur
    sketch = np.minimum(255, 256 * (grayscale / (1e-6 + blur)))
    sketch = sketch.astype(np.uint8)
    return original, sketch


def display_result(original, sketch, save_path=None):
    panel = np.zeros((original.shape[0], 2 * original.shape[1], 3), dtype=np.uint8)
    sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    panel[:, :original.shape[1]] = original
    panel[:, original.shape[1]:] = sketch
    if save_path is not None:
        cv2.imwrite(os.path.expanduser(save_path + '/sketch.jpg'), sketch)
    cv2.imshow("Before vs. After", panel)
    cv2.waitKey(0)


def main():
    path = input("Enter the path name: ")
    if path == "":
        path = 'dawg.png'
    save_path = input("Enter where should the image be saved: ")
    original, sketch = pencil_sketch(image_path=path)
    display_result(original, sketch, save_path)


if __name__ == "__main__":
    main()

