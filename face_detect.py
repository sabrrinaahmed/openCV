import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1] #gets the image name from command line arguments
cascPath = "haarcascade_frontalface_default.xml" #xml file has cascade, which contains the data to detect faces

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath) #creates an instance of cascade and loads image into memory so it is ready to use

# Read the image
image = cv2.imread(imagePath) #reads image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert image to grayscale (many operations in OpenCV are done in grayscale)

# Detect faces in the image
faces = faceCascade.detectMultiScale(   #detectMultiScale is general function that detects objects
    gray,                               #grayscale image
    scaleFactor=1.1,                    #compensates for how close the faces are to the camera
    minNeighbors=5,                     #defines how many objects are detected near the current one before it declares the face found
    minSize=(30, 30),                   #gives the size of each window
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)                                       #returns list of faces believed to be found

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:             #returns the x and y location of rectangle, and w and h of rectangle
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) #draws a rectangle around found faces

cv2.imshow("Faces found", image)       #displays image
cv2.waitKey(0)