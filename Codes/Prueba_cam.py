#THIS IS THE BASE PROGRAM FOR THE FINAL PROTOTYPE

#Functions from Keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
#from keras.layers import Conv2D, MaxPooling2D
#from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

#For preprocessing the image
from keras.preprocessing.image import array_to_img, img_to_array, load_img

#Import Opencv and rest
import numpy as np
import cv2
import time
import sys

#Images size
img_width, img_height = 125, 125

#Some verifications
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)


#Loading pretrained model
model=load_model('chest_final.h5')

#Obtaining images from cameras
android = cv2.VideoCapture("http:192.168.42.2:8080/video")
android.set(cv2.CAP_PROP_FPS,1)
#yicam = cv2.VideoCapture("rtsp://192.168.42.1/live")

palabra=""
letra='A'
key=0

while(True):

    while(True):

        # Capture frame-by-frame
        ret, frame_android= android.read()
        #ret, frame_yicam= yicam.read()

        # Display the resulting frame
        #cv2.imshow('frame',frame_yicam)
        cv2.imshow('frame 2',frame_android)

        # Our operations on the frame come here
        frame_android = cv2.resize(frame_android,(img_width,img_height))  

        #generates arrays
        x = img_to_array(frame_android)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        #predict 
        out = model.predict(x)
        result = np.where(out == np.amax(out))
    
        #Print
        if(result[1][0]==0):
            sys.stdout.write("\rB--->")
            letra='B'
        if(result[1][0]==1):
            sys.stdout.write("\rC--->")
            letra='C'
        if(result[1][0]==2):
            sys.stdout.write("\rD--->")
            letra='D'
        if(result[1][0]==3):
            sys.stdout.write("\rE--->")
            letra='E'
        if(result[1][0]==4):
            sys.stdout.write("\rF--->")
            letra='F'
        if(result[1][0]==5):
            sys.stdout.write("\rG--->")
            letra='G'
        if(result[1][0]==6):
            sys.stdout.write("\rH--->")
            letra='H'
        if(result[1][0]==7):
            sys.stdout.write("\rI--->")
            letra='I'
        if(result[1][0]==8):
            sys.stdout.write("\rL--->")
            letra='L'
        if(result[1][0]==9):
            sys.stdout.write("\rO--->")
            letra='O'
        if(result[1][0]==10):
            sys.stdout.write("\rP--->")
            letra='P'
        if(result[1][0]==11):
            sys.stdout.write("\rQ--->")
            letra='Q'
        if(result[1][0]==12):
            sys.stdout.write("\rR--->")
            letra='R'
        if(result[1][0]==13):
            sys.stdout.write("\rT--->")
            letra='T'
        if(result[1][0]==14):
            sys.stdout.write("\rU--->")
            letra='U'
        if(result[1][0]==16):
            sys.stdout.write("\rW--->")
            letra='W'
        if(result[1][0]==17):
            sys.stdout.write("\rX--->")
            letra='X'

        #leer entrada
        key = cv2.waitKey(1)

        if key == 13:
            palabra=palabra+letra
            break
        elif key == 32:
            palabra=palabra + ' '
            break
        elif key == 27:
            break

    sys.stdout.write("\r"+"          "+palabra)

    if key==27: 
        break

print("Adios!!!!!!")
