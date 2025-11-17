from src.keys import pico_voice_key
import pvporcupine


class Wake:
    def __enter__(self):
        try:
            self.porcupine = pvporcupine.create(
                access_key=f"{pico_voice_key()}",
                keyword_paths=["assets/wakeword/Flubber_en_raspberry-pi_v3_0_0.ppn"],
            )
        except:
            self.porcupine = pvporcupine.create(
                access_key=f"{pico_voice_key()}", keywords=["computer"]
            )

        print("purcupine started")
        return self

    def get_device_frame_length(self):
        return self.porcupine.frame_length

    def listen_until_woken(self, recorder):
        while True:
            audio_frame = recorder.read()
            keyword_index = self.porcupine.process(audio_frame)
            if keyword_index >= 0:
                print(f"Heard keyword {keyword_index}")
                return

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.porcupine.delete()
