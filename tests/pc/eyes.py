# This file is meant to run stand-alone on gui environment.
# It mimics Flobbers eyes without the hardware for testing complex eye logics.

from threading import Timer
from src.eyes.eyestates import *
from PIL import Image, ImageDraw


class MockDisplay:
    def prepare_image(self, image):
        return image


class Eyes:
    margin = 40
    screen = 240
    tilt = 10.4

    def __init__(self):
        self.displayL = MockDisplay()
        self.displayR = MockDisplay()
        self.timer = None
        self.glasses = Image.new(
            "RGBA",
            (self.margin * 4 + self.screen * 3, self.margin * 2 + self.screen),
            "white",
        )

        draw = ImageDraw.Draw(self.glasses)
        draw.ellipse(
            (0, 0, self.margin * 2 + self.screen, self.margin * 2 + self.screen),
            outline="orange",
            fill=(0, 0, 0, 0),
            width=self.margin,
        )
        draw.ellipse(
            (
                self.margin * 2 + self.screen * 2,
                0,
                self.margin * 4 + self.screen * 3,
                self.margin * 2 + self.screen,
            ),
            outline="orange",
            fill=(0, 0, 0, 0),
            width=self.margin,
        )

    def set_state(self, eyeState: Animation):
        if self.timer is not None:
            self.timer.cancel()
        eyeState.init([self.displayL, self.displayR])
        self.eyeState = eyeState
        self.update()

    def update(self):
        if self.eyeState is None:
            return
        images = self.eyeState.update()
        self.set_image(images)

        if self.eyeState.update_interval() > 0:
            self.timer = Timer(self.eyeState.update_interval(), self.update)
            self.timer.start()

    def set_image(self, images):

        combined = Image.new(
            "RGBA",
            (self.margin * 4 + self.screen * 3, self.margin * 2 + self.screen),
            "white",
        )

        combined.paste(
            images[1].rotate(
                180 + self.tilt, resample=Image.Resampling.BICUBIC, expand=False
            ),
            (self.margin, self.margin),
        )
        combined.paste(
            images[0].rotate(
                180 - self.tilt, resample=Image.Resampling.BICUBIC, expand=False
            ),
            (self.margin * 3 + self.screen * 2, self.margin),
        )

        Image.alpha_composite(combined, self.glasses).show()


if __name__ == "__main__":
    eyes = Eyes()
    while True:
        selection = input(
            "Select eye state:\n1. Off\n2. Open\n3. Blinking\n4. Clock\n(Ctrl + C to quit)\n> "
        )
        match selection:
            case "1":
                eyes.set_state(Off())
            case "2":
                eyes.set_state(FullOpen())
            case "3":
                eyes.set_state(Blinking())
            case "4":
                eyes.set_state(ClockMode())
