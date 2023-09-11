import cv2
import numpy as np

def otsu_single(image_path):
    gray = cv2.imread(image_path,0) 

    # Calculate the histogram
    hist = []
    for i in range(255):
        hist.append(np.count_nonzero(gray == i))
    hist = np.array(hist)
    hist_np = hist
    hist = 1.0*hist/np.sum(hist)

    mean_num = range(255)*hist

    variances = []
    # Calculating the between class variances
    max_var = 0
    T = 0
    for i in range(1,255):
        W_b = sum(hist[:i])
        W_f = sum(hist[i:])
        mean_b = sum(mean_num[:i])/(sum(hist[:i])+0.00001)
        mean_f = sum(mean_num[i:])/(sum(hist[i:])+0.00001)

        var_i = (W_b*W_f)*((mean_b-mean_f)**2)
        variances.append(var_i)
        if var_i > max_var:
            max_var = var_i
            T = i
    return T, hist_np