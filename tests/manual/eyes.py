from src.eyes.eyes import Eyes
import src.eyes.eyestates as states

request = input("Enter eye state (Off, Open, Blinking): ")


def get_state(request: str):
    match request.lower():
        case "open":
            return states.FullOpen()
        case "off":
            return states.Off()
        case "blinking":
            return states.Blinking()
        case "blink":
            return states.BlinkOnce()
    return None


with Eyes() as eyes:
    while get_state(request) is not None:
        eyes.set_state(get_state(request))
        request = input("Enter eye state (Off, Open, Blinking): ")
