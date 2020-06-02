#Programa que aumenta artificialmente el dataset añadiéndole nuevos backgrounds

import cv2
import numpy as np

# Read the images
frame = cv2.imread("original.jpg")
background = cv2.imread("background.jpg")

#Create alpha layer using a mask
min = np.array([140,0,0])
max = np.array([255,255,255])

#Create a png from the original image with transparent background
frame2 = cv2.cvtColor(frame, cv2.COLOR_RGBTOHSV)
alpha = cv2.inRange(frame, min, max)

# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255
b, g, r = split(frame);
rgba = [b, g, r, alpha]
dst = cv2.merge(rgba, 4)
cv2.imwrite("test.png", dst)

# Convert uint8 to float
frame = foreground.astype(float)
background = background.astype(float)

# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, frame)

# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)

# Add the masked foreground and background.
outImage = cv2.add(foreground, background)

# Display image
cv2.imshow("outImg", outImage/255)
cv2.waitKey(0)


