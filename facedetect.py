# Block of code for automatic path setup: it makes possible
# to execute the script from any location as long as the
# input file(s) are in the same folder as the script.
import os
abpath = os.path.abspath(__file__)
script_path = os.path.dirname(abpath)
os.chdir(script_path)

# Importing OpenCV
import cv2

# Loading the cascade classifier:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# --- Change the name of your picture below: ---
image = cv2.imread('picture_name_here.jpg')
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Processing image and retrieving faces:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image,
scaleFactor=1.1,
minNeighbors=5)

# A face is identified by a Numpy array: x and y are
# the coordinates of the top-left point of the rectangle
# containing the face, then height and width of the rectangle
print(faces)

# Drawing rectangle(s) over face(s), updating 'image'.
# The parameters are the coordinates of the top-left and 
# lower-right points of the rectangle, plus the values in RGB
# for color, and line weight.
for x, y, h, w in faces:
    image = cv2.rectangle(image, (x, y),(x + w, y + h), (0, 255, 0),3)
# Resizing before showing picture:
resized = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))
cv2.imshow('Picture window', resized)
cv2.waitKey(0)
cv2.destroyAllWindows