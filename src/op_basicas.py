# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:41:39 2018

@author: Javier
"""
import cv2 
import numpy as np
from image_resize import image_resize as configura

#algunas transformaciones geométricasa< con Python + OpenCV

#%%
#Scaling

img = cv2.imread('vintage.jpg')
res = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
#a continuación llamamos a una función creada por nosotros
res2 = configura(img,1080*4,720*4,inter = cv2.INTER_AREA) 
cv2.imwrite("pequenio.jpg", res)
cv2.imwrite("grande.jpg", res2)

#%%
#traslación de imágenes en Python

img = cv2.imread('vintage.jpg')
num_rows, num_cols = img.shape[:2]
#float32 es equivalente al float de Python, 
translation_matrix = np.float32([ [1,0.5,90], [0,1,60] ])
#----------------------------------a b c     d e f
#a activa matriz imagen entrada
#b deforma imagen horizontal
#c traslada lateral
#d deforma imagen vertical
#e activa imagen entrada salida
#f traslada imagen verticalmente
#cuando desplazas, vas dejando píxeles "vacíos", puestos a 0. el 0 es el color negro.

img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
#transformación afín  m2=a*m1+b
#donde m1 es la imagen original, m2 la imagen a la que se aplica cambio
#a es la transformación lineal / deformación, b es desplazamiento / traslado
cv2.imshow('Translation', img_translation)
cv2.waitKey()
#%%
#rotacion
img = cv2.imread('vintage.jpg')
rows,cols = img.shape[:2]
imageRotation = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(img,imageRotation,(cols,rows))
cv2.imshow('Rotation', dst)
cv2.waitKey()
#%%
#operaciones de perspectiva
img = cv2.imread('sudoku-original.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

perspective = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,perspective,(300,300))

cv2.imshow('Perspective', dst)
cv2.waitKey()
#%%
#Image filtering

#smooth

import cv2
import numpy as np


img = cv2.imread('vintage.jpg')

kernel = np.ones((15,15),np.float32)/225
smoothed = cv2.filter2D(res,-3,kernel)

cv2.imshow('smooth',smoothed)
cv2.waitKey()

#%%
import cv2
import numpy as np
img2 = cv2.imread('vintage.jpg')

res = cv2.medianBlur(img2,5)
cv2.imshow('medianBlur',res)
cv2.waitKey()
#%%
import cv2
import numpy as np
img2 = cv2.imread('vintage.jpg')

res = cv2.GaussianBlur(img2,(5,5),0)
cv2.imshow('GaussianBlur',res)
cv2.waitKey()

