# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 21:51:01 2018

@author: Javier
"""

import numpy as np
import cv2

img = cv2.imread('restaurar.jpg')
mask = cv2.imread('mask.jpg',0)


mask[np.logical_and(mask>0, mask < 246)] = 0 
cv2.imshow('mask',mask)
dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()