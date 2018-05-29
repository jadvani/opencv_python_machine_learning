# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:56:39 2018

@author: Javier
"""
'''
Cuando queremos ampliar MUCHO una imagen, solemos verla pixelada. 
interpolación: obtención de nuevos puntos partiendo 
del conocimiento de un conjunto discreto de puntos
Podríamos crear una nueva imagen de más resolución, 
aproximando los píxeles sin resolver


Sugerencia: probar otros algoritmos de interpolación:
INTER_NEAREST - a nearest-neighbor interpolation
INTER_LINEAR - a bilinear interpolation (used by default)
INTER_AREA - resampling using pixel area relation. It may be a preferred method 
for image decimation, as it gives moire’-free results. But when the image is zoomed, 
it is similar to the INTER_NEAREST method.
INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood
'''
import cv2
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized