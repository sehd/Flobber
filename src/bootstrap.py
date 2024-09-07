def bootstrap(start_main_loop):
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

    import settings

    print(f"Selected mic: {mics[settings.get_mic_device_id()]}")
    with Wake() as wake:
        print(f"Starting wake. Frame length = {wake.get_device_frame_length()}")
        with Mic(
            settings.get_mic_device_id(), wake.get_device_frame_length()
        ) as recorder:
            recorder.start_recorder()

            print("Recording test file... make some noise")
            testRecordingPath = "output/testRecording.wav"
            recorder.record_test_file(testRecordingPath)
            recorder.stop_recorder()

            print("Playing back")

            from speak import play

            play(testRecordingPath)
            print(f"Test recording saved in {testRecordingPath}")

            print("Listening ... (press Ctrl+C to exit)")
            try:
                start_main_loop(recorder, wake)
            except KeyboardInterrupt:
                tts.say_offline("Flubber shut down")
                print("Stopping ...")
            except Exception as ex:
                if hasattr(ex, "message"):
                    tts.say_offline(ex.message)
                else:
                    tts.say_offline(ex)
