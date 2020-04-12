# -*- coding: utf-8 -*-

import cv2
import numpy as np


base_path=""
img_fn = [base_path+"img0b.jpg", base_path+"img1b.jpg", base_path+"img3b.jpg"]
images = [cv2.imread(x) for x in img_fn]
times = np.array([4.09, 1.18, -1.82])
times *= 1000.
merger = cv2.createMergeDebevec()
hdr = merger.process(images, times)
cv2.imshow('out.jpg', hdr)