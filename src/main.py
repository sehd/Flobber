from stt import transcribe_audio_openai
from speak import play
import chatgpt
from commands import time, askchatgpt


def start_main_loop(recorder, wake):
    supported_commands = _supported_commands.keys()
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
        selected_command = chatgpt.get_intent_from_input(command, supported_commands)
        supported_commands[selected_command](recorder=recorder,command=command)

def unknown_command(**kwargs):
    print(f"Command not found {kwargs["command"]}")

_supported_commands = {
    "None":unknown_command,
    "Ask a question": askchatgpt.ask_chatgpt,
    "What time is it": time.what_time_is_it,
}
