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

        list_dir = os.listdir(img_dir)
        for f in re.search("^*p{}*cropped.jpg$".format(trapNum), list_dir):
            print("-> Sending cropped image :: {}".format(f))
            gfile = self.drive.CreateFile({'parents' : [{'id' : self.folders['cropped']}], 'title' : f})
            gfile.SetContentFile(f)
            gfile.Upload()
        for f in re.search("^*p{}*.png$".format(trapNum), list_dir):
            print("-> Sending original image :: {}".format(f))
            gfile = self.drive.CreateFile({'parents' : [{'id' : self.folders['original']}], 'title' : f})
            gfile.SetContentFile(f)
            gfile.Upload()