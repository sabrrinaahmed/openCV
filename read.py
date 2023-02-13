import cv2 as cv

# Reading pictures
img = cv.imread('Photos/cat.jpeg') #takes in the path for an image and returns an image as a matrix of pixels

cv.imshow('Cat', img) #displays image as new window, parameters (name of window, matrix of pixels)

cv.waitKey(0) #waits for time in milliseconds for a key to be pressed, 0 = infinite amount of time

#Reading Videos
