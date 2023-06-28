#! -*- Coding: utf-8 -*-

import re
import os
import threading

#Credentials
from google.oauth2.credentials import Credentials
from pydrive.drive import GoogleDrive # Pydrive library (pip install pydrive)
from pydrive.auth import GoogleAuth

class DriveUploader:
    folders = {
    # dataset 5MP
        'cropped': '1dcpawBB2w5mPP1AZMXoGDyNpEO7hzc2U',
        'original': '1ddAydzhwpoIwpqt78H4HSAj03_7lvy01'
    
    # dataset 8MP
        #'cropped': '1V_2FZw5X9T828xQedEOvb5l9lsr6Zoac',
        #'original': '1Lzn6tLnREkbgqlCT3tHNDqCrPoUyYZqN'
    }

    def __init__(self, gauth):
        self.gauth = GoogleAuth()
        self.gauth.LoadCredentialsFile("settings.yaml")
        self.drive = GoogleDrive(self.gauth)

    def startPlateUpload(self, trapNum):
        def realStartPlateUpload():
            img_dir = os.path.abspath("../img")
            
            cropName = re.compile('.*cropped.*')
            originalName = re.compile('.*\.png.*')
            print("\n [***] UPLOADING TO DRIVE [***]\n")
            c = 0
            for f in os.listdir(img_dir):
                c += 1
                filename = os.path.join(img_dir, f)
                #print("Arquivo: " + str(filename))
            
                try:
                    #print("Entrou no try")
                    #re.search("^p{}*cropped\.jpg$".format(trapNum), filename)
                    if cropName.match(filename):  # Cropped images
                        print("----> Sending cropped image :: {}".format(filename))
                        gfile = self.drive.CreateFile({'parents' : [{'id' : self.folders['cropped']}], 'title' : f})
                        gfile.SetContentFile(filename)
                        gfile.Upload()
                        os.remove(filename) # Remove file
                        print("---[*] Uploaded Cropped image:: {}\n".format(filename))
                    elif originalName.match(filename):
                        print("----> Sending original image :: {}".format(filename))
                        gfile = self.drive.CreateFile({'parents' : [{'id' : self.folders['original']}], 'title' : f})
                        gfile.SetContentFile(filename)
                        gfile.Upload()
                        os.remove(filename) # Remove file
                        print("---[*] Uploaded Original image:: {}\n".format(filename))
                except re.error as e:
                    print("Regex Error return {}".format(e))
            print(" [***] UPLOAD COMPLETED [***]\n")
        threading.Thread(target=realStartPlateUpload).start()
