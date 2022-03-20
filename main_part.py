# importing all libraries needed to read all files
import glob
import cv2
import numpy as np


# lets create size of a patch, which is adjustable
# then less size_of_patch then better quality of result image
# but it increase Time Complexity as far as code have to consider and calculate more parts
# of the original image
size_of_patch = 40


# first of all I would like to create a DB for our project in order to use the in future
# in my case I used files only with jpg extension, but it works in the same way with "png" and "gif"
dataset = [cv2.resize(cv2.imread(file), (size_of_patch, size_of_patch)) for file in glob.glob("dataset/*.jpg")]


# at the same time we have to create storage of all colors
colors = np.array([cv2.resize(cv2.imread(file), (size_of_patch, size_of_patch)).mean(axis=0).mean(axis=0) for file in
                   glob.glob("dataset/*.jpg")])


# now lets upload original image and read it
original = cv2.imread("target/input2.jpg")


# now lets get the dimensions of original image
rows, columns, layers = original.shape


# now based on the original image we know its dimensions, by that reason lets create new clear array
# and after that will work on it, initially it is dark image
# reference was taken here:
# https://stackoverflow.com/questions/12881926/create-a-new-rgb-opencv-image-using-python
result = np.zeros((rows, columns, 3), np.uint8)

for i in range(int(columns / size_of_patch)):
    for j in range(int(rows / size_of_patch)):
        # taking one fragment of original image
        fragment = original[j * size_of_patch: (j + 1) * size_of_patch, i * size_of_patch: (i + 1) * size_of_patch, :]

        # calculating its average color as it was done before
        fragment_color = fragment.mean(axis=0).mean(axis=0)

        # measuring euclidian distance between currently selected fragment and all dataset that was uploaded
        euclidean_distance = np.linalg.norm(fragment_color - colors, axis=1)

        # substituting part of our final image from the black background to the one that most of all
        # satisfies currently selected part, it can be done via sort or choosing one that has the smallest difference
        result[j * size_of_patch: (j + 1) * size_of_patch, i * size_of_patch: (i + 1) * size_of_patch, :] = \
            dataset[np.argmin(euclidean_distance)]

# saving final result
cv2.imwrite("target/Nolan2.jpg", result)

