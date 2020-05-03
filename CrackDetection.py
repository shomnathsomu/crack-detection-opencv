# importing necessary libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read a cracked sample image
img = cv2.imread('samples/query_06.bmp')

# Convert into gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Inverting / negative image
imgNeg = cv2.bitwise_not(gray)

# Apply logarithmic transform
img_log = (np.log(imgNeg+1)/(np.log(1+np.max(imgNeg))))*255

# Specify the data type
img_log = np.array(img_log,dtype=np.uint8)

# Image smoothing: bilateral filter
bilateral = cv2.bilateralFilter(img_log, 5, 75, 75)

# Canny Edge Detection
edges = cv2.Canny(bilateral,400,500)
