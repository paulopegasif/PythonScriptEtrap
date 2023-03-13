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
        print("[*] Starting Picamera2 configuration method")
        self.picam.configure(self.picam_config)
        
    def startPlateCapture(self, trapNum):
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
                
                # Saving image file
                img_string = "{}_p{}_{}_{}.png".format(
                    str(date.today()).replace("-", ""), 
                    trapNum,
                    bug_name,
                    self.lastImageId)
                img_conv.save(img_string)
                c += 1
        cv2.destroyAllWindows()