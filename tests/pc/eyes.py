# This file is meant to run stand-alone on gui environment.
# It mimics Flobbers eyes without the hardware for testing complex eye logics.

# import sys
# import os
from threading import Thread, Timer
from src.eyes.eyestates import *

# sys.path.append(os.getcwd())


class MockDisplay:
    def prepare_image(self, image):
        return image


class Eyes:
    displayL = MockDisplay()
    displayR = MockDisplay()
    timer = None

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

    def set_image(self, image):
        image[0].rotate(180).show()
        image[1].rotate(180).show()


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
