from tts import say_openai
from speak import play
from stt import transcribe_audio_openai
import chatgpt
from localization import get_localized

def ask_chatgpt(**kwargs):
    recorder = kwargs["recorder"]
    play(get_localized('AUDIO_SURE'))
    command_path = "output/command.wav"
    recorder.start_recorder()
    recorder.record_until_silence(command_path)
    recorder.stop_recorder()
    play("assets/predefined_sounds/emm.mp3", block=False)
    command = transcribe_audio_openai(command_path)
    gpt_response = chatgpt.get_chatgpt_response(command)
    say_openai(gpt_response)
