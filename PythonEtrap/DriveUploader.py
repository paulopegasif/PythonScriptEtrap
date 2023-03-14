#! -*- Coding: utf-8 -*-

import re
import os
from pydrive.drive import GoogleDrive # Pydrive library (pip install pydrive)

class DriveUploader:
    folders = {
        'cropped': '[FOLDER_ID]',
        'original': '[FOLDER_ID]'
    }

    def __init__(self, gauth):
        self.gauth = gauth
        self.drive = GoogleDrive(self.gauth)

    def startPlateUpload(self, trapNum):
        img_dir = os.path.abspath("./")
        search = re.compile('*_{}_*_cropped.jpg'.format(trapNum))

        c = 0
        for f in os.listdir(img_dir):
            c += 1
            filename = os.path.join(img_dir, f)

            if search.match(filename):  # Cropped images
                print("Cropped")
                gfile = self.drive.CreateFile({'parents' : [{'id' : self.folder['cropped']}], 'title' : f})
                gfile.SetContentFile(filename)
                gfile.Upload()

            else:                       # Original images
                print("Originals")
                gfile = self.drive.CreateFile({'parents' : [{'id' : self.folder['original']}], 'title' : f})
                gfile.SetContentFile(filename)
                gfile.Upload()