from array import array

from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *
x=342
y=423
xd=208
yd=444
xtree=162
ytree=437
class Cordinates():
    replaybutton=(x,y)
    dinosaur=(xd,yd)
def restartgame():
    pyautogui.click(Cordinates.replaybutton)
    pyautogui.keyDown('down')
def pressspace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.18)
    print("Jump")
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imagegrab():
    box=(Cordinates.dinosaur[0]+60 ,Cordinates.dinosaur[1],
         Cordinates.dinosaur[0]+150,Cordinates.dinosaur[1]+5)
    image=ImageGrab.grab(box)
    grayimage=ImageOps.grayscale(image)
    a=array(grayimage.getcolors())

    return a.sum()


def main():
    restartgame()
    while True:
        if(imagegrab()!=447):
            pressspace()
        if(imagegrab()!=447):
            print(imagegrab())
main()

