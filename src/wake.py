from keys import pico_voice_key
import pvporcupine


class Wake:
    def __enter__(self) -> None:
        self.porcupine = pvporcupine.create(
            access_key=f"{pico_voice_key()}",
            keyword_paths=["assets/wakeword/Flubber_en_raspberry-pi_v3_0_0.ppn"],
        )

    def get_device_frame_length(self):
        return self.porcupine.frame_length

    def listen_until_woken(self, recorder):
        while True:
            audio_frame = recorder.read()
            keyword_index = self.porcupine.process(audio_frame)
            if keyword_index == 0:
                print("Flubber!!!!")
                return

    def __exit__(self):
        self.porcupine.delete()
