from src.memory.log import log, log_error
import src.tts as tts
from src.ears.mic import Mic, get_mics
from src.ears.wake import Wake
import src.memory.settings as settings
from playsound3 import playsound, AVAILABLE_BACKENDS, DEFAULT_BACKEND
from src.eyes.eyes import Eyes
from src.eyes.eyestates import BlinkOnce
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
        log_error("No microphone found.")
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
                eyes.set_state(BlinkOnce())
                log("Listening ...")
                try:
                    start_main_loop(recorder, wake, eyes)
                except KeyboardInterrupt:
                    log("Stopping ...")
                except Exception as ex:
                    if hasattr(ex, "message"):
                        log_error(ex.message)
                    else:
                        log_error(ex)


if __name__ == "__main__":
    try:
        bootstrap()
    except Exception as ex:
        log_error(ex)
