import cv2
import numpy as np
import matplotlib.pyplot as plt
from Otsu import otsu_single
from multi_thresh import otsu_multi

levels = 1

image_path = './original image.jpg'
gray = cv2.imread(image_path,0)

if levels == 1:
    T, hist_np = otsu_single(image_path)
    Mask = (gray >= T).astype(np.uint8) * 255
else:
    T, hist_np = otsu_multi(image_path, levels)
    Mask = np.digitize(gray, T)

plt.subplot(131)
plt.imshow(gray, cmap='gray')
plt.subplot(132)
# plt.hist(im_flat, bins=256, range=(0, 255))
plt.bar(range(hist_np.shape[0]), hist_np)
if levels == 1:
    plt.axvline(x=T, color='red', linestyle='-', label=f'Red Line at {T}')
    plt.title(f'The threshold value is {T}')
else:
    for i in range(levels):
        plt.axvline(x=T[i], color='red', linestyle='-', label=f'Red Line at {T}')
        plt.title(f'The threshold values are {T}')
plt.subplot(133)
plt.imshow(Mask, cmap='gray')
plt.show()
