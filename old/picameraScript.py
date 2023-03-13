from picamera2 import Picamera2, Preview
from PIL import Image
import time
import cv2


def tirarFoto():
    NOME_ARQUIVO = "imagem.png"

    picam2 = Picamera2()
    camera_config = picam2.create_video_configuration(main={"size": (2028, 1080)})
    camera_config["controls"]['FrameDurationLimits'] = (33333, 33333)
    camera_config["controls"]['NoiseReductionMode'] = 1

    picam2.configure(camera_config)
    #picam2.start_preview(Preview.QTGL)
    picam2.start()

    time.sleep(1)
    #picam2.capture_file("test.jpg")
    while True:
        img = picam2.capture_array()
        
        cv2.imshow("Frame", img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        elif key == ord("p"):
            img_conv = Image.fromarray(img)
            img_conv.save(NOME_ARQUIVO)
    cv2.destroyAllWindows()