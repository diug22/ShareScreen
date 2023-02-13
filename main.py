import numpy as np
import cv2
from mss import mss
from PIL import Image
from pynput.mouse import Button, Controller,Listener

coor = []
position = ['Haz click en la esquina superior derecha de tu pantalla.','Haz click para la altura.','Haz click para la anchura.']


def on_click(x, y, button, pressed):
    if pressed:
        coor.append((x, y))
    if not pressed:
        # Stop listener
        return False


def manual_configuration():
    for p in position:
        print(p)
        with Listener(
            on_click=on_click) as listener:
                listener.join()
    listener.stop()


if __name__ == "__main__":
    manual_configuration()
    print(coor)
    bounding_box = {'top': coor[0][1], 'left': coor[0][0], 'width': coor[2][0]-coor[0][0], 'height': coor[1][1]-coor[0][1]}

    sct = mss()

    while True:
        sct_img = sct.grab(bounding_box)
        image = np.array(sct_img)
        
        up_width = 1980
        up_height = 1200
        up_points = (up_width, up_height)
        resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)
        
        cv2.imshow('screen',resized_up)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
