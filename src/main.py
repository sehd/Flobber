print("Starting up...")


print("Testing tts...")

import tts

tts.say_offline("Starting up")

print("Starting mic...")

from mic import Mic, get_mics
from wake import Wake

mics = [x for x in get_mics()]
print("\n".join(mics))
if len(mics) == 0:
    print("No microphone found.")
    exit()

print(f"Selected mic: {mics[0]}")
print("Starting wake word service...")
with Wake() as wake:
    with Mic(0, wake.get_device_frame_length()) as recorder:
        recorder.start_recorder()
        print("Listening ... (press Ctrl+C to exit)")
        try:
            wake.listen_until_woken(recorder)
        except KeyboardInterrupt:
            tts.say_offline("Flubber shut down")
            print("Stopping ...")
