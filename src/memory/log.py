from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler

Path("output/logs").mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("Flobber")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    "output/logs/app.log",
    when="midnight",
    interval=1,
    backupCount=14,
    encoding="utf-8",
)

handler.setFormatter(
    logging.Formatter(
        "%(asctime)s\t%(levelname)s:\t%(message)s",
        datefmt="%H:%M:%S",
    )
)

logger.addHandler(handler)


def log(content):
    logger.info(content)
    print(content)


def log_error(content):
    logger.error(content)
    print(f"Error:{content}")


def log_warning(content):
    logger.warning(content)
    print(f"Warning:{content}")
