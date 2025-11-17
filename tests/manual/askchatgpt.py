from src.commands.askchatgpt import ask_chatgpt
from src.mic import Mic
import src.settings as settings

if __name__ == "__main__":
    with Mic(settings.get_mic_device_id(), 512) as recorder:
        ask_chatgpt(recorder=recorder)