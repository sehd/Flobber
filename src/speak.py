from playsound3 import playsound


def play(path, block=True):
    playsound(path, block=block, backend="ffplay")
