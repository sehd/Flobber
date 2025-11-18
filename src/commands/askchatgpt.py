from src.tts import say_openai
from src.stt import transcribe_audio_openai
import src.chatgpt as chatgpt
from src.localization import play_localized, LocalizedSounds


def ask_chatgpt(**kwargs):
    recorder = kwargs["recorder"]
    play_localized(LocalizedSounds.OfCourse)

    print("Listening for your question...")
    command_path = "output/command.wav"
    recorder.start_recorder()
    recorder.record_until_silence(command_path)
    print("Silence detected")
    recorder.stop_recorder()

    play_localized(LocalizedSounds.Emm, block=False)

    command = transcribe_audio_openai(command_path)
    ask_chatgpt_directly(command=command)


def ask_chatgpt_directly(**kwargs):
    question = kwargs["command"]
    gpt_response = chatgpt.get_chatgpt_response(question)
    say_openai(gpt_response)
