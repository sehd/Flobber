import sys
import os
import spidev as SPI
from threading import Thread, Timer
from memory.log import log, Level
from eyestates import Animation, Off

sys.path.append(os.getcwd())
from lib import LCD_1inch28


class Eyes:
    def __init__(self) -> None:
        self.displayL = LCD_1inch28.LCD_1inch28(
            spi=SPI.SpiDev(0, 0), rst=27, dc=25, bl=6
        )
        self.displayR = LCD_1inch28.LCD_1inch28(
            spi=SPI.SpiDev(1, 0), rst=22, dc=24, bl=12
        )

        # Initialize library.
        self.displayL.Init()
        self.displayR.Init()

    def __enter__(self) -> None:
        # Clear display.
        self.set_state(Off())

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.timer is not None:
            self.timer.cancel()
        self.set_state(Off())
        self.displayL.module_exit()
        self.displayR.module_exit()

    def set_state(self, eyeState: Animation):
        if self.timer is not None:
            self.timer.cancel()
        eyeState.init([self.displayL, self.displayR])
        self.state = eyeState
        self.update()

    def update(self):
        if self.state is None:
            return
        images = self.state.update()
        self.set_image(images)

        if self.eyeState.update_interval() > 0:
            Timer(self.eyeState.update_interval(), self.update).start()

    def set_image(self, image):
        def write(display, buf):
            try:
                display.show_prepared_image(buf)
            except Exception as e:
                log(f"Error writing image to display: {e}", Level.Error)

        t1 = Thread(target=write, args=(self.displayL, image[0]), daemon=True)
        t2 = Thread(target=write, args=(self.displayR, image[1]), daemon=True)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
