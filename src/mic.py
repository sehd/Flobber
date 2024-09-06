from pvrecorder import PvRecorder
import wave
import struct


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

    def record_test_file(self, path):
        wav_file = wave.open(path, "w")
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(16000)
        for _ in range(100):
            pcm = self.recorder.read()
            wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))
        wav_file.close()

    def read(self):
        return self.recorder.read()
