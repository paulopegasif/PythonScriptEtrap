#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from tkinter import simpledialog
from picamera2 import Picamera2
from PIL import Image
from datetime import date

class Camera:
    picam = Picamera2()
    
    def __init__(self, shotWidth=2048, shotHeight=1080, frames=33):
        self.shotWidth = shotWidth;
        self.shotHeight = shotHeight;
        self.frames = frames * 1010;        # Converting frames to hz
        self.makeDefaultConfig()
    
    def makeDefaultConfig(self):
        self.picam_config = self.picam.create_video_configuration(
            main={"size": (self.shotWidth, self.shotHeight)})
        self.picam_config['controls']['FrameDurationLimits'] = (self.frames, self.frames)
        self.picam_config['controls']['NoiseReductionMode'] = 1
        
    def configure(self):
        ''' Define Picamera2 configuration & User defined settings '''
        print("[*] Starting Picamera2 configuration method")
        self.picam.configure(self.picam_config)
        
    def startPlateCapture(self, trapNum):
        ''' PiCamera2 frame capture loop with Opencv2 image interface '''
        self.trapNum = trapNum

        # Start picamera
        self.picam.start()
        
        # Data capture array
        c = 1
        while True:
            # Getting numpy image array from camera module
            img = self.picam.capture_array()
            
            # Showing frame & getting any user input
            cv2.imshow("Frame", img)
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord("q"):
                break
            elif key == ord("p"):
                self.imageShot(img)
                c += 1
        cv2.destroyAllWindows()

    def imageShot(self, img):
        ''' Take a image shot from opencv camera module (picamera numpy array)
            @arg img ==> Numpy array
        '''
         # Get image from frame numpy array
        img_conv = Image.fromarray(img)
        
        # Getting user insect name (GUI)
        bug_name = simpledialog.askstring(
            title="Etrap - Loop de captura",
            prompt="Qual o nome do inseto? (Acesso rapido: 1=>Afideo; 2=>Parasitoide)")
        
        if bug_name == '1':
            bug_name = "afideo"
        elif bug_name == '2':
            bug_name = "parasitoide"
        
        # Saving image file (original)
        img_string = "{}_p{}_{}_{}".format(
            str(date.today()).replace("-", ""), 
            self.trapNum,
            bug_name,
            self.lastImageId)
        img_string_png = img_string + ".png"
        img_conv.save(img_string_png)

        # Image cropping object
        mid_img = 608 / 2
        img_crop = cv2.imread(img_string_png)
        print("[*] Cropping image '" + img_string_png + "'...\n", img_crop.shape)

        # Image dimensions
        height, width, c = img_crop.shape
        print("\theight:" + str(height/2) + "\n\twidth:" + str(width/2))

        # Cropping data shape
        img_cropped = img_crop[(int)(height/2 - mid_img):(int) (height/2 + mid_img), (int)(width/2 - mid_img): (int) (width/2 + 304)]
        cv2.imwrite(img_string + "_cropped.jpg", img_cropped)