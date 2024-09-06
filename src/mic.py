from pvrecorder import PvRecorder


def get_mics():
    for i, device in enumerate(PvRecorder.get_available_devices()):
        yield "Device %d: %s" % (i, device)


def start_recorder(device_id, frame_length):
    recorder = PvRecorder(frame_length=frame_length, device_index=device_id)
    recorder.start()
    return recorder


def stop_recorder(recorder):
    recorder.delete()
