from settings import get_language
from speak import play
from enum import Enum

with open(f"assets/{get_language()}/strings.csv") as strings:
    _localized_values = {x.split(",")[0]: x.split(",")[1] for x in strings.readlines()}


def get_localized_string(key):
    return _localized_values[key]


LocalizedSounds = Enum("predefined_sounds", names={"Yes": "yes.mp3", "Emm": "emm.mp3"})


def play_localized(sound: LocalizedSounds, block=True):
    play(f"assets/{get_language()}/{sound.value}", block=block)
