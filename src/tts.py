import pyttsx3
from openai import OpenAI
from speak import play
from keys import openai_api_key
import os


def _change_voice(engine, language, gender="female"):
    for voice in engine.getProperty("voices"):
        if voice.id == language and gender == voice.gender:
            engine.setProperty("voice", voice.id)
            return

    for voice in engine.getProperty("voices"):
        if voice.id == language:
            engine.setProperty("voice", voice.id)
            return

    engine.setProperty("voice", 0)


def say_offline(text):
    engine = pyttsx3.init()
    _change_voice(engine, "English (Great Britain)")
    engine.setProperty

    engine.say(text)
    engine.runAndWait()


def say_openai(text):
    client = OpenAI(api_key=openai_api_key())
    speech_file_path = "output/openai.mp3"
    if os.path.exists(speech_file_path):
        os.remove(speech_file_path)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.write_to_file(speech_file_path)
    play(speech_file_path)


# say_openai("Emmm...")
