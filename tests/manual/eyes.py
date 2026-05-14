from src.eyes.eyes import Eyes
from src.eyes.eyestates import FullOpen, Off, Blinking

request = input("Enter eye state (Off, Open, Blinking): ")


def get_state(request: str):
    if request.lower() == "open":
        return FullOpen()
    if request.lower() == "Off":
        return Off()
    if request.lower() == "Blinking":
        return Blinking
    return None


with Eyes() as eyes:
    while get_state(request is not None):
        eyes.set_state(get_state(request))
        state = input("Enter eye state (Off, Open, Close, Blinking, Heart): ")
