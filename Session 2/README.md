#  Circle Detection Project

### A Python project for detecting circles in images and videos using OpenCV. 


---

## Features
- Detects circles in static images and video streams.
- Visualizes detected circles directly on the media.
- Adjustable detection parameters for fine-tuning sensitivity.

---

##  Project Structure
```

.
├── adjustable_circle_detector.py (bonus 1)
├── circle_detector.py (basic script)
├── video_circle_detector.py (bonus 2)
├── notebook.ipynb (scrapbook)
├── test1.png
├── test2.jpg
├── test3.png 
├── result1.jpg 
├── result2.jpg 
├── result3.jpg 
└── statistics.txt

```

---




## Usage

You will be prompted for an image path.
 
Save directory (optional)
   - If provided, the output is saved as `sketch.jpg`

---

##  How It Works
1. Convert the image to grayscale  
2. Apply Gaussian blur  
3. Detect circles using `cv2.HoughCircles()` function  
4. Visualise detected circles over the original image


---

## Output

The output displays a window showing side-by-side comparison of the input and the output.

---

## Challenges
There were initially a lot of overlaps between circles and it was identifying a lot of noise as circles as well. But then on adjusting and fine-tuning the parameters, the issue got resolved to a reasonable extent.
