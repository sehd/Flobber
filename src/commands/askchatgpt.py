from tts import say_openai
from speak import play
from stt import transcribe_audio_openai
import chatgpt


def ask_chatgpt(**kwargs):
    recorder = kwargs["recorder"]
    play("assets/predefined_sounds/yes.mp3")
    command_path = "output/command.wav"
    recorder.start_recorder()
    recorder.record_until_silence(command_path)
    recorder.stop_recorder()
    play("assets/predefined_sounds/emm.mp3", block=False)
    command = transcribe_audio_openai(command_path)
    gpt_response = chatgpt.get_chatgpt_response(command)
    say_openai(gpt_response)
