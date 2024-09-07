from stt import transcribe_audio
from speak import play
from bootstrap import bootstrap


def start_main_loop(recorder, wake):
    while True:
        wake.listen_until_woken(recorder)
        play("assets/predefined_sounds/yes.mp3")
        command_path = "output/command.wav"
        recorder.record_until_silence(command_path)
        command = transcribe_audio(command_path)


bootstrap(start_main_loop)
