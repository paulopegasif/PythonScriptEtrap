#! -*- Coding: utf-8 -*-

import re
import os
from pydrive.drive import GoogleDrive # Pydrive library (pip install pydrive)

class DriveUploader:
    folders = {
        'cropped': '1V_2FZw5X9T828xQedEOvb5l9lsr6Zoac',
        'original': '1Lzn6tLnREkbgqlCT3tHNDqCrPoUyYZqN'
    }

    def __init__(self, gauth):
        self.gauth = gauth
        self.drive = GoogleDrive(self.gauth)

    def startPlateUpload(self, trapNum):
        img_dir = os.path.abspath("./")

        c = 0
        for f in os.listdir(img_dir):
            c += 1
            filename = os.path.join(img_dir, f)

            if re.search("^*p{}*cropped.jpg$".format(trapNum), filename):  # Cropped images
                print("-> Sending cropped image :: {}".format(filename))
                gfile = self.drive.CreateFile({'parents' : [{'id' : self.folders['cropped']}], 'title' : f})
                gfile.SetContentFile(filename)
                gfile.Upload()
            elif re.search("^*p{}*.png$".format(trapNum), filename):
                print("-> Sending original image :: {}".format(filename))
                gfile = self.drive.CreateFile({'parents' : [{'id' : self.folders['original']}], 'title' : f})
                gfile.SetContentFile(filename)
                gfile.Upload()