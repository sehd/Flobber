from src.eyes.eyes import Eyes
from src.eyes.eyestates import FullOpen,Off
from time import time

with Eyes() as eyes:
    frames = 0
    start_time = time()
    while True:
        eyes.set_state(FullOpen())
        eyes.set_state(Off())
        frames += 2
        if frames % 100 == 0:
            print(f"{frames/(time()-start_time)} FPS")
