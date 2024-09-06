print("Starting up...")


print("Testing tts...")

import tts

tts.say_offline("Starting up")

print("Starting mic...")

import mic
from wake import Wake

mics = [x for x in mic.get_mics()]
print("\n".join())
print(f"Selected mic: {mics[0]}")
print("Starting wake word service...")
with Wake() as wake:
    with mic.start_recorder(0, wake.get_device_frame_length()) as recorder:
        print("Listening ... (press Ctrl+C to exit)")
        try:
            wake.listen_until_woken(recorder)
        except KeyboardInterrupt:
            tts.say_offline("Flubber shut down")
            print("Stopping ...")
