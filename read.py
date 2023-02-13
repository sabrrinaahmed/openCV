import cv2 as cv

# Reading pictures
#img = cv.imread('Photos/cat.jpeg') #takes in the path for an image and returns an image as a matrix of pixels

#cv.imshow('Cat', img) #displays image as new window, parameters (name of window, matrix of pixels)

#cv.waitKey(0) #waits for time in milliseconds for a key to be pressed, 0 = infinite amount of time

#Reading Videos
capture = cv.VideoCapture('Videos/tennis.MOV') #cameras references with 0, 1, and so on
#capture variable is an instance of the Video capture class

#Reads in video frame by frame and returns the frame and a boolean that says whether the frame was successfully read in or not
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame) # show each frame

    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter D is pressed, then break loop and stop displaying the video
        break

capture.release()
cv.destroyAllWindows()