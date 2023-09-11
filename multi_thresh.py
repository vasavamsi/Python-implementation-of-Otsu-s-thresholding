import numpy as np
import matplotlib.pyplot as plt
import cv2

def otsu_multi(image_path, lev):

    image = cv2.imread(image_path, 0)
    # Calculate histogram
    hist, _ = np.histogram(image, bins=256, range=(0, 256))
    p = hist / np.sum(hist)

    # Calculate global mean
    uG = np.dot(np.arange(256), p)

    # For N = 2
    if lev == 2:
        max_var = 0
        for t1 in range(256):
            for t2 in range(t1 + 1, 256):
                p1 = np.sum(p[:t1 + 1])
                p2 = np.sum(p[t1 + 1:t2 + 1])
                p3 = np.sum(p[t2 + 1:])

                if p1 == 0 or p2 == 0 or p3 == 0:
                    continue

                u1 = np.dot(np.arange(t1 + 1), p[:t1 + 1]) / p1
                u2 = np.dot(np.arange(t1 + 1, t2 + 1), p[t1 + 1:t2 + 1]) / p2
                u3 = np.dot(np.arange(t2 + 1, 256), p[t2 + 1:]) / p3

                in_between_variance = (u1 - uG) ** 2 * p1 + (u2 - uG) ** 2 * p2 + (u3 - uG) ** 2 * p3
                if in_between_variance > max_var:
                    max_var = in_between_variance
                    thresh = [t1, t2]

    # For N > 2
    else:
        max_var = 0
        for t1 in range(256):
            for t2 in range(t1 + 1, 256):
                for t3 in range(t2 + 1, 256):
                    p1 = np.sum(p[:t1 + 1])
                    p2 = np.sum(p[t1 + 1:t2 + 1])
                    p3 = np.sum(p[t2 + 1:t3 + 1])
                    p4 = np.sum(p[t3 + 1:])

                    if p1 == 0 or p2 == 0 or p3 == 0 or p4 == 0:
                        continue

                    u1 = np.dot(np.arange(t1 + 1), p[:t1 + 1]) / p1
                    u2 = np.dot(np.arange(t1 + 1, t2 + 1), p[t1 + 1:t2 + 1]) / p2
                    u3 = np.dot(np.arange(t2 + 1, t3 + 1), p[t2 + 1:t3 + 1]) / p3
                    u4 = np.dot(np.arange(t3 + 1, 256), p[t3 + 1:]) / p4

                    in_between_variance = (u1 - uG) ** 2 * p1 + (u2 - uG) ** 2 * p2 + (u3 - uG) ** 2 * p3 + (u4 - uG) ** 2 * p4
                    if in_between_variance > max_var:
                        max_var = in_between_variance
                        thresh = [t1, t2, t3]

    return thresh, hist

