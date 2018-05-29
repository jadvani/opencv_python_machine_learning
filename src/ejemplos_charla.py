# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 11:46:50 2018

@author: Javier
"""
#primer ejemplo con opencv!
import cv2
import numpy as np
originalImage= cv2.imread('vintage.jpg')
cv2.imshow('Star Wars',originalImage)
cv2.waitKey()

#%%
#vamos a redimensionar la imagen

scalingImage = cv2.resize(originalImage,(0,0),fx=0.5,fy=0.5)

#la vamos a hacer más grande
from image_resize import image_resize as configura
imageBigger = configura(originalImage,1080*2,720*2,inter=cv2.INTER_AREA)
cv2.imwrite('bigger.jpg',imageBigger)
#%%
#translating images
num_rows,num_cols=originalImage.shape[:2]
translationMatrix=np.float32([[1,0,100],[0.5,1,30]])
imgTranslation=cv2.warpAffine(originalImage,translationMatrix,(num_cols,num_rows))

cv2.imshow('imagen trasladada',imgTranslation)
cv2.waitKey()
#%%
#operaciones de perspectiva
img=cv2.imread('sudoku-original.jpg')
rows,cols,ch=img.shape
pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
perspectiveImage=cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,perspectiveImage,(300,300))
cv2.imshow('arreglada',dst)
cv2.waitKey()

#%%
