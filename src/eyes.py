import time
import sys
import os
import spidev as SPI
from enum import Enum
from threading import Timer
from PIL import Image

sys.path.append(os.getcwd())
from lib import LCD_1inch28

EyeStates = Enum("EyeStates", ["Off", "Blinking", "Open", "Close"])

width = 240
height = 240


class Eyes:
    def __init__(self) -> None:
        # Load images
        self.openImages = [
            Image.open("assets/eyes/RightEyeOpen.jpg"),
            Image.open("assets/eyes/LeftEyeOpen.jpg"),
        ]
        self.closeImage = [
            Image.open("assets/eyes/RightEyeClose.jpg"),
            Image.open("assets/eyes/LeftEyeClose.jpg"),
        ]
        self.blackImage = Image.new("RGB", (width, height), "BLACK")
        self.timer = Timer()

    def __enter__(self) -> None:
        self.displayL = LCD_1inch28.LCD_1inch28(
            spi=SPI.SpiDev(0, 0), rst=27, dc=25, bl=6
        )
        self.displayR = LCD_1inch28.LCD_1inch28(
            spi=SPI.SpiDev(1, 0), rst=22, dc=24, bl=12
        )
        # Initialize library.
        self.displayL.Init()
        self.displayR.Init()
        # Clear display.
        self.set_state(EyeStates.Off)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.displayL.clear()
        self.displayR.clear()
        self.displayL.module_exit()
        self.displayR.module_exit()

    def set_state(self, eyeState: EyeStates):
        self.timer.cancel()
        if eyeState == EyeStates.Off:
            self.set_image(self.blackImage)
            self.currentState = eyeState
        elif eyeState == EyeStates.Blinking:
            if eyeState != EyeStates.Open:
                self.set_state(self.openImages)
                self.currentState = EyeStates.Open
                self.timer.interval = 3
            else:
                self.set_image(self.closeImage)
                self.currentState = EyeStates.Close
                self.timer.interval = 0.2
            self.timer.function = lambda: self.set_state(EyeStates.Blinking)
            self.timer.start()

    def set_image(self, image):
        self.displayR.ShowImage(image[0])
        self.displayL.ShowImage(image[1])


print("Starting")
with Eyes() as eyes:
    print("Started")
    time.sleep(3)
    print("Starting blink")
    eyes.set_state(EyeStates.Blinking)
    time.sleep(3)
    print("Background working")

    time.sleep(3)
    print("Background working")
    time.sleep(3)
    print("Background working")
    time.sleep(3)
    print("Background working")
    time.sleep(3)
    print("Background working")

    print("Closing")
    eyes.set_state(EyeStates.Off)

    time.sleep(3)

print("Done")
