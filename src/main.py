from stt import transcribe_audio_openai
from speak import play
from bootstrap import bootstrap
from chatgpt import get_chatgpt_response
from tts import say_openai


def start_main_loop(recorder, wake):
    while True:
        recorder.start_recorder()
        wake.listen_until_woken(recorder)
        recorder.stop_recorder()
        play("assets/predefined_sounds/yes.mp3")
        command_path = "output/command.wav"
        recorder.start_recorder()
        recorder.record_until_silence(command_path)
        recorder.stop_recorder()
        play("assets/predefined_sounds/emm.mp3", block=False)
        command = transcribe_audio_openai(command_path)
        gpt_response = get_chatgpt_response(command)
        say_openai(gpt_response)


bootstrap(start_main_loop)
