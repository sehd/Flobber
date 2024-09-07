from pvrecorder import PvRecorder
import wave
import struct
import numpy as np

SILENCE_THRESHOLD = 500
SILENCE_DURATION = 1


def get_mics():
    for i, device in enumerate(PvRecorder.get_available_devices()):
        yield "Device %d: %s" % (i, device)


def _is_silent(data_chunk):
    """Returns 'True' if below the silence threshold"""
    audio_data = np.array(data_chunk, dtype=np.int16)
    return np.max(audio_data) < SILENCE_THRESHOLD


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

    def record_until_silence(self, path, max_seconds=15):
        silence_chunk_limit = int(
            SILENCE_DURATION * self.recorder.sample_rate / self.frame_length
        )
        total_chunk_limit = int(
            max_seconds * self.recorder.sample_rate / self.frame_length
        )

        total_chunks = 0
        silent_chunks = 0
        frames = []

        while True:
            pcm = self.recorder.read()
            frames.append(struct.pack("h" * len(pcm), *pcm))
            total_chunks += 1
            if _is_silent(pcm):
                silent_chunks += 1
            else:
                silent_chunks = 0

            if total_chunks > total_chunk_limit or silent_chunks > silence_chunk_limit:
                print("Stopped command recording")
                break

        wav_file = wave.open(path, "w")
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(self.recorder.sample_rate)
        wav_file.writeframes(b"".join(frames))
        wav_file.close()

    def record_test_file(self, path):
        wav_file = wave.open(path, "w")
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(self.recorder.sample_rate)
        for _ in range(100):
            pcm = self.recorder.read()
            wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))
        wav_file.close()

    def read(self):
        return self.recorder.read()
