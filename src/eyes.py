import time
import sys
import os

sys.path.append(os.getcwd())
from lib import LCD_1inch28

from PIL import Image

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #display = LCD_1inch28.LCD_1inch28(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    display = LCD_1inch28.LCD_1inch28()
    # Initialize library.
    display.Init()
    # Clear display.
    display.clear()
    while True:
        image = Image.open('assets/eyes/LeftEyeOpen.jpg')
        display.ShowImage(image)
        time.sleep(3)
        image = Image.open('assets/eyes/LeftEyeClose.jpg')
        display.ShowImage(image)
        time.sleep(0.2)
    display.module_exit()
except IOError as e:
    print("Error in eyes module:")
    print(e)
except KeyboardInterrupt:
    display.clear()
    display.module_exit()
    
