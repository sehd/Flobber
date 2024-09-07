import os


def get_mic_device_id():
    return os.environ.get("FLOBBER_MIC_ID", 0)


def total_recording_length():
    return os.environ.get("FLOBBER_TOTAL_COMMAND_LENGTH", 15)
