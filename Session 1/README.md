{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww17280\viewh13000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs36 \cf0 #  Pencil Sketch Generator\
\
### A Python script that converts images into a pencil sketch effect using OpenCV.\
\
---\
\
## Features\
- Pencil sketch effect from any image  \
- Optional saving of the output image  \
\
\
---\
\
##  Project Structure\
```\
.\
\uc0\u9500 \u9472 \u9472  pencil_sketch.py\
\uc0\u9500 \u9472 \u9472  README.md\
\uc0\u9492 \u9472 \u9472  dawg.png   # default image\
```\
\
---\
\
\
\
\
## Usage\
\
You will be prompted for an image path.\
   - Press `Enter` to use the default image (`dawg.png`)\
\
Save directory (optional)\
   - If provided, the output is saved as `sketch.jpg`\
\
---\
\
##  How It Works\
1. Convert the image to grayscale  \
2. Invert the grayscale image  \
3. Apply Gaussian blur  \
4. Divide and scale image  \
\
Formula used:\
```\
sketch = min(255, 256 * (gray / (blur + \uc0\u949 )))\
```\
for each pixel in the B&W image.\
\
---\
\
## Output\
\
The output displays a window showing side-by-side comparison of the input and the output.\
\
---\
\
## Challenges\
For some reason the scaled matrix wasn't showing up on using `cv2.imshow()` and that was because the pixels in the array were saved as floats. Didn't help by converting them to ints either. Finally found out OpenCV needed values saved in `np.uint8` datatype.}