from keys import pico_voice_key
import pvporcupine
from pvrecorder import PvRecorder

porcupine = pvporcupine.create(
    access_key=f"{pico_voice_key()}",
    keywords=["bumblebee"],
)


def get_next_audio_frame():
    return recorder.read()


def listen_until_woken():
    while True:
        audio_frame = get_next_audio_frame()
        keyword_index = porcupine.process(audio_frame)
        if keyword_index == 0:
            print("Flubber!!!!")
            porcupine.delete()
            return


# for i, device in enumerate(PvRecorder.get_available_devices()):
#     print("Device %d: %s" % (i, device))
recorder = PvRecorder(frame_length=porcupine.frame_length, device_index=0)
recorder.start()

print("Listening ... (press Ctrl+C to exit)")
try:
    listen_until_woken()
except KeyboardInterrupt:
    print("Stopping ...")
finally:
    recorder.delete()
    porcupine.delete()
