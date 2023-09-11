# https-github.com-vasavamsi-Python-implementation-of-Otsu-s-thresholding

Otsu is a thresholding method used to differentiate the pixels into foreground and background by calculating the maximum variance between both classes. The method can be further formulated to digitize the picture into more than two classes. In this file I showed the algorithm followed to code this method along with the results obtained. Instructions to use the code are also included. 

I completed this code using python. I used cv2, numpy and matplotlib libraries to complete the task.

## Algorithm

_Step 1_: Convert the input image into Grayscale.

_Step 2_: calculate the histogram profile and normalize.

_Step 3_: Multiply the histogram values with their corresponding pixel values.

_Step 4_: Calculate the in between variance for each pixel.
