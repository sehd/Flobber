from pvrecorder import PvRecorder


def get_mics():
    for i, device in enumerate(PvRecorder.get_available_devices()):
        yield "Device %d: %s" % (i, device)


class Mic:
    def __init__(self, device_id, frame_length):
        self.device_id = device_id
        self.frame_length = frame_length

    def __enter__(self):
        self.recorder = PvRecorder(
            frame_length=self.frame_length, device_index=self.device_id
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.recorder.delete()

    def start_recorder(self):
        self.recorder.start()

    def stop_recorder(self):
        self.recorder.stop()

    def read(self):
        return self.recorder.read()
