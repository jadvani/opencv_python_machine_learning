# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:42:19 2018

@author: Javier
"""

import cv2
import numpy as np
from image_resize import image_resize as configura
img = cv2.imread('imagenes dif exposicion\monumento\img3.jpg')
res2 = configura(img,1080,720,inter = cv2.INTER_AREA) 
cv2.imwrite('imagenes dif exposicion\monumento\img3b.jpg', res2)