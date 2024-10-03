import time
import sys
import os
import spidev as SPI
from PIL import Image

sys.path.append(os.getcwd())
from lib import LCD_1inch28
from lib.lcdconfig import RaspberryPi

try:
    display0 = LCD_1inch28.LCD_1inch28(
        RaspberryPi(spi=SPI.SpiDev(0, 0), rst=27, dc=25, bl=6)
    )
    display1 = LCD_1inch28.LCD_1inch28(
        RaspberryPi(spi=SPI.SpiDev(1, 1), rst=22, dc=24, bl=12)
    )

    # Initialize library.
    display0.Init()
    display1.Init()
    # Clear display.
    display0.clear()
    display1.clear()
    while True:
        image = Image.open("assets/eyes/LeftEyeOpen.jpg")
        display0.ShowImage(image)
        display1.ShowImage(image)
        time.sleep(3)
        image = Image.open("assets/eyes/LeftEyeClose.jpg")
        display0.ShowImage(image)
        display1.ShowImage(image)
        time.sleep(0.2)
except IOError as e:
    print("Error in eyes module:")
    print(e)
except KeyboardInterrupt:
    display0.clear()
    display1.clear()
    display0.module_exit()
    display1.module_exit()
