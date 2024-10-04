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
        self.displayR = LCD_1inch28.LCD_1inch28(
            spi=SPI.SpiDev(1, 0), rst=22, dc=24, bl=12
        )
        self.displayL = LCD_1inch28.LCD_1inch28(
            spi=SPI.SpiDev(0, 0), rst=27, dc=25, bl=6
        )
        # Initialize library.
        self.displayR.Init()
        self.displayL.Init()
        # Load images
        self.openImages = [
            self.displayR.prepare_image(Image.open("assets/eyes/RightEyeOpen.jpg")),
            self.displayL.prepare_image(Image.open("assets/eyes/LeftEyeOpen.jpg")),
        ]
        self.closeImage = [
            self.displayR.prepare_image(Image.open("assets/eyes/RightEyeClose.jpg")),
            self.displayL.prepare_image(Image.open("assets/eyes/LeftEyeClose.jpg")),
        ]
        self.blackImage = [
            self.displayR.prepare_image(Image.new("RGB", (width, height), "BLACK")),
            self.displayL.prepare_image(Image.new("RGB", (width, height), "BLACK")),
        ]
        self.timer = Timer(0, self.set_state, [EyeStates.Off])

    def __enter__(self) -> None:
        # Clear display.
        self.set_state(EyeStates.Off)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.set_state(EyeStates.Off)
        self.displayL.module_exit()
        self.displayR.module_exit()

    def set_state(self, eyeState: EyeStates):
        print(f"Setting state {eyeState}")
        self.timer.cancel()
        if eyeState == EyeStates.Off:
            self.set_image(self.blackImage)
            self.currentState = eyeState
        elif eyeState == EyeStates.Blinking:
            if self.currentState != EyeStates.Open:
                self.set_image(self.openImages)
                self.currentState = EyeStates.Open
            else:
                self.set_image(self.closeImage)
                self.currentState = EyeStates.Close
            self.timer = Timer(
                3 if self.currentState == EyeStates.Open else 0.2,
                self.set_state,
                [EyeStates.Blinking],
            )
            self.timer.start()

    def set_image(self, image):
        self.displayR.show_prepared_image(image[0])
        self.displayL.show_prepared_image(image[1])


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
