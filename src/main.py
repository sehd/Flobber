from src.eyes import EyeStates
from src.stt import transcribe_audio_openai
import src.chatgpt as chatgpt
from src.commands import time, askchatgpt
from src.localization import play_localized, LocalizedSounds


def start_main_loop(recorder, wake, eyes):
    while True:
        recorder.start_recorder()
        wake.listen_until_woken(recorder)
        recorder.stop_recorder()
        play_localized(LocalizedSounds.Yes)
        command_path = "output/command.wav"
        recorder.start_recorder()
        recorder.record_until_silence(command_path)
        recorder.stop_recorder()
        eyes.set_state(EyeStates.Blinking)
        play_localized(LocalizedSounds.Emm)
        command = transcribe_audio_openai(command_path)
        selected_command = chatgpt.get_intent_from_input(command, _supported_commands.keys())
        _supported_commands[selected_command](recorder=recorder, command=command)
        eyes.set_state(EyeStates.Off)


def unknown_command(**kwargs):
    print(f"Command not found {kwargs['command']}")


_supported_commands = {
    "None": unknown_command,
    "Ask a question": askchatgpt.ask_chatgpt,
    "What time is it": time.what_time_is_it,
}
