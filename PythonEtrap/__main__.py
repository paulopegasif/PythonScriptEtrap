#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Camera
import DriveUploader
from tkinter import simpledialog
from pydrive.auth import GoogleAuth
import tkinter



def main():
    
    # Camera object context
    cam = Camera.Camera()
    cam.configure()

    # Google Drive Object
    gauth = GoogleAuth()
    gdrive = DriveUploader.DriveUploader(gauth)
    
    # Insect traps loop
    
    tkroot= tkinter.Tk()
    while True:
        trapNum = simpledialog.askinteger(
            title="Etrap - Loop de captura",
            prompt="Escreva o ID da placa de captura")
        cam.startPlateCapture(trapNum)
        gdrive.startPlateUpload(trapNum)

if __name__ == "__main__":
    main()
