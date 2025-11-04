import time
import sys
import os
import spidev as SPI
from enum import Enum
from threading import Timer
from PIL import Image

sys.path.append(os.getcwd())
from lib import LCD_1inch28

EyeStates = Enum(
    "EyeStates", ["Off", "Open", "HalfOpen", "Close", "Blinking", "BlinkOnce", "Heart"]
)

width = 240
height = 240


def load_image(path: str) -> Image.Image:
    image = Image.open(path)
    return image.rotate(180)


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
            self.displayR.prepare_image(load_image("assets/eyes/Open.jpg")),
            self.displayL.prepare_image(load_image("assets/eyes/Open.jpg")),
        ]
        self.halfOpenImages = [
            self.displayR.prepare_image(load_image("assets/eyes/HalfOpen.jpg")),
            self.displayL.prepare_image(load_image("assets/eyes/HalfOpen.jpg")),
        ]
        self.closeImages = [
            self.displayR.prepare_image(load_image("assets/eyes/Close.jpg")),
            self.displayL.prepare_image(load_image("assets/eyes/Close.jpg")),
        ]
        self.blackImages = [
            self.displayR.prepare_image(Image.new("RGB", (width, height), "BLACK")),
            self.displayL.prepare_image(Image.new("RGB", (width, height), "BLACK")),
        ]
        self.heartImages = [
            self.displayR.prepare_image(load_image("assets/eyes/Heart.jpg")),
            self.displayL.prepare_image(load_image("assets/eyes/Heart.jpg")),
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
            self.set_image(self.blackImages)
            self.currentState = eyeState
        elif eyeState == EyeStates.Open:
            self.set_image(self.openImages)
            self.currentState = eyeState
        elif eyeState == EyeStates.Close:
            self.set_image(self.closeImages)
            self.currentState = eyeState
        elif eyeState == EyeStates.Heart:
            self.set_image(self.heartImages)
            self.currentState = eyeState
        elif eyeState == EyeStates.Blinking:
            if self.currentState == EyeStates.Close:
                self.set_image(self.openImages)
                self.currentState = EyeStates.Open
                sleep = 3
            elif self.currentState == EyeStates.HalfOpen:
                self.set_image(self.closeImages)
                self.currentState = EyeStates.Close
                sleep = 0.2
            elif self.currentState == EyeStates.Open:
                self.set_image(self.halfOpenImages)
                self.currentState = EyeStates.HalfOpen
                sleep = 0.1
            else:
                self.set_image(self.closeImages)
                self.currentState = EyeStates.Close
                sleep = 0.2
            self.timer = Timer(
                sleep,
                self.set_state,
                [EyeStates.Blinking],
            )
            self.timer.start()
        elif eyeState == EyeStates.BlinkOnce:
            self.set_image(self.openImages)
            time.sleep(1)
            self.set_state(EyeStates.Close)
            self.timer = Timer(1, self.set_state, [EyeStates.Off])
            self.timer.start()

    def set_image(self, image):
        self.displayR.show_prepared_image(image[0])
        self.displayL.show_prepared_image(image[1])
