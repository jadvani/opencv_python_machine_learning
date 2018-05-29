# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:27:12 2018

@author: Javier
"""

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
import utils

 
# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread('porgs.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)

# cluster the pixel intensities
# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))
clt = KMeans(n_clusters = 10)

nx, ny = image.shape


clt.fit(image)


# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
