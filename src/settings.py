import os


def get_mic_device_id():
    return int(os.environ.get("FLOBBER_MIC_ID", "0"))


def total_recording_length():
    return int(os.environ.get("FLOBBER_TOTAL_COMMAND_LENGTH", "15"))


def silence_threshold():
    return int(os.environ.get("FLOBBER_SILENCE_THRESHOLD", "1000"))


def silence_duration():
    return int(os.environ.get("FLOBBER_SILENCE_DURATION", "1"))


def enable_mic_test_on_bootstrap():
    return os.environ.get("FLOBBER_MIC_TEST_ON_BOOTSTRAP", "True") == "True"


def get_language():
    return os.environ.get("FLOBBER_LANGUAGE", "en")
