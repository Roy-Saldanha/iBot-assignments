#  Pencil Sketch Generator

### A Python script that converts images into a pencil sketch effect using OpenCV.

---

## Features
- Pencil sketch effect from any image  
- Optional saving of the output image  


---

##  Project Structure
```
.
├── pencil_sketch.py
├── README.md
├── dawg.png   (default image)
└── video_sketch.py (bonus)
```

---




## Usage

You will be prompted for an image path.
   - Press `Enter` to use the default image (`dawg.png`)

Save directory (optional)
   - If provided, the output is saved as `sketch.jpg`

---

##  How It Works
1. Convert the image to grayscale  
2. Invert the grayscale image  
3. Apply Gaussian blur  
4. Divide and scale image  

Formula used:
```
sketch = min(255, 256 * (gray / (blur + ε)))
```
for each pixel in the B&W image.

---

## Output

The output displays a window showing side-by-side comparison of the input and the output.

---

## Challenges
For some reason the scaled matrix wasn't showing up on using `cv2.imshow()` and that was because the pixels in the array were saved as floats. Didn't help by converting them to ints either. Finally found out OpenCV needed values saved in `np.uint8` datatype.
