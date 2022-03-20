from PIL import Image
import numpy as np
import math

# Create the following 1000 x 1000 8-bit images; include a picture and the Matlab* commands you used in your writeup.
side = 1000


# 1.1) A grayscale image of constant intensity 100
data = np.zeros((side, side, 3), dtype=np.uint8)
data[0:1000, 0:1000] = [100, 100, 100]
img1 = Image.fromarray(data)
img1.save('img1.png')


# 1.2) A grayscale image with alternating black and white vertical stripes, each of which is 4 pixels wide
data = np.zeros((side, side, 3), dtype=np.uint8)
for y in range(0, 1000, 8):
    data[0:1000, y:y + 4] = [255]
img2 = Image.fromarray(data)
img2.save('img2.png')


# 1.3) A grayscale image with a ramp intensity distribution, described by I(x, y) = x/2
data = np.zeros((side, side, 3), dtype=np.uint8)
for row in range(1000):
    for column in range(1000):
        data[row, column] = [column/4]
img3 = Image.fromarray(data)
img3.save('img3.png')


# 1.4) A grayscale image with a Gaussian intensity distribution centered at (128, 128), described by
data = np.zeros((side, side, 3), dtype=np.uint8)
for row in range(1000):
    for column in range(1000):
        power = - ((row - 524) ** 2 + (column - 524) ** 2) / 200 ** 2
        data[row, column] = 255 * math.exp(power)
img4 = Image.fromarray(data)
img4.save('img4.png')


# 1.5) A color image where the upper left quadrant is yellow, the lower left quadrant is red, the upper right
# quadrant is green, and the lower right quadrant is black
data = np.zeros((side, side, 3), dtype=np.uint8)
for row in range(0, 500):
    # upper left - yellow
    for column in range(0, 500):
        data[row, column] = [255, 255, 0]
    # lower left - red
    for column in range(500, 1000):
        data[row, column] = [0, 128, 0]

for row in range(500, 1000):
    # upper right - green
    for column in range(0, 500):
        data[row, column] = [255, 0, 0]
    # lower right - black
    for column in range(500, 1000):
        data[row, column] = [0, 0, 0]

img5 = Image.fromarray(data)
img5.save('img5.png')
