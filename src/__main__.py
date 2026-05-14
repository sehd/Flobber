from memory.log import log, Level
import src.tts as tts
from src.mic import Mic, get_mics
from src.wake import Wake
import src.settings as settings
from playsound3 import playsound, AVAILABLE_BACKENDS, DEFAULT_BACKEND
from src.eyes import Eyes, EyeStates
from src.main import start_main_loop


def test_mic(recorder):
    recorder.start_recorder()

    print("Recording test file... make some noise")
    testRecordingPath = "output/testRecording.wav"
    recorder.record_test_file(testRecordingPath)
    recorder.stop_recorder()

    print("Playing back")

    from src.speak import play

    play(testRecordingPath)
    print(f"Test recording saved in {testRecordingPath}")


def bootstrap():
    log("Starting up...")

    tts.say_offline("Starting up")

    mics = [x for x in get_mics()]
    log("\n".join(mics))
    if len(mics) == 0:
        log("No microphone found.", Level.Error)
        exit()

    log(f"Selected mic: {mics[settings.get_mic_device_id()]}")

    with Wake() as wake:
        log(f"Starting wake. Frame length = {wake.get_device_frame_length()}")
        with Mic(
            settings.get_mic_device_id(), wake.get_device_frame_length()
        ) as recorder:
            if settings.enable_mic_test_on_bootstrap():
                test_mic(recorder)

            with Eyes() as eyes:
                eyes.set_state(EyeStates.BlinkOnce)
                log("Listening ...")
                try:
                    start_main_loop(recorder, wake, eyes)
                except KeyboardInterrupt:
                    log("Stopping ...")
                except Exception as ex:
                    if hasattr(ex, "message"):
                        log(ex.message, Level.Error)
                    else:
                        log(ex, Level.Error)


if __name__ == "__main__":
    bootstrap()
