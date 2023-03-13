#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Camera
from tkinter import simpledialog

def main():
    # Camera object context
    cam = Camera()
    cam.configure()
    
    # Insect traps loop
    while True:
        trapNum = simpledialog.askinteger(
            title="Etrap - Loop de captura",
            prompt="Escreva o ID da placa de captura")
        cam.startPlateCapture(trapNum)

if __name__ == "__main__":
    main()
