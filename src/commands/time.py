from datetime import datetime
from tts import say_offline


def what_time_is_it(**kwargs):
    t = datetime.now().strftime("It's %H %M")
    print(t)
    say_offline(t)
