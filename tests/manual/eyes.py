from src.eyes.eyes import Eyes
from src.eyes.eyestates import FullOpen, Off, Blinking

request = input("Enter eye state (Off, Open, Blinking): ")


def get_state(request: str):
    if request.lower() == "open":
        return FullOpen()
    if request.lower() == "off":
        return Off()
    if request.lower() == "blinking":
        return Blinking()
    return None


with Eyes() as eyes:
    while get_state(request) is not None:
        eyes.set_state(get_state(request))
        request = input("Enter eye state (Off, Open, Blinking): ")
