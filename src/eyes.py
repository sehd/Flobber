import time
import sys
import os

sys.path.append(os.getcwd())
from lib import LCD_1inch28

from PIL import Image
from spidev import SPI

m0Config = {"RST": 27, "DC": 25, "BL": 6, "bus": 0, "device": 0}

m1Config = {"RST": 22, "DC": 24, "BL": 12, "bus": 1, "device": 1}
try:
    display0 = LCD_1inch28.LCD_1inch28(
        spi=SPI.SpiDev(m0Config["bus"], m0Config["device"]),
        spi_freq=10000000,
        rst=m0Config["RST"],
        dc=m0Config["DC"],
        bl=m0Config["BL"],
    )
    display1 = LCD_1inch28.LCD_1inch28(
        spi=SPI.SpiDev(m1Config["bus"], m1Config["device"]),
        spi_freq=10000000,
        rst=m1Config["RST"],
        dc=m1Config["DC"],
        bl=m1Config["BL"],
    )
    # display = LCD_1inch28.LCD_1inch28()
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
