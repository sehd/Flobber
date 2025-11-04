from src.eyes import Eyes, EyeStates
from time import time

with Eyes() as eyes:
    frames=0
    start_time = time()
    while True:
        eyes.set_state(EyeStates.Open)
        eyes.set_state(EyeStates.Close)
        frames+=2
        if frames%1000==0:
            print(f"{frames/(time()-start_time)} FPS")
