from enum import Enum
from datetime import date, datetime

currentDate = None
file = None

Level = Enum("Level", ["Error", "Warning", "Info"])


def log(content, level: Level = Level.Info):
    if file is None or currentDate != date.today():
        currentDate = date.today()
        file = open("output/logs/{currentDate}.txt", "at")

    file.write(f"{datetime.now().time()}\t{level}: \t{content}\n")
    file.flush()
    print(content)
