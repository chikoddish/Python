'''
Write a python script that can detect faces in an image and save all the faces in a folder
'''
import cv2
# Load the cascade
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')
# Read the input image
img = cv2.imread('images/amitabh.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
faces = eye_cascade.detectMultiScale(gray, 1.3, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    crop_face = img[y:y + h, x:x + w]
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', crop_face)
# Display the output
cv2.imshow('img', img)
cv2.imshow("imgcropped", crop_face)
cv2.waitKey()
