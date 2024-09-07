import pyttsx3
from openai import OpenAI
from speak import play
from keys import openai_api_key
import os


def say_offline(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 150)

    engine.say(text)
    engine.runAndWait()


def say_openai(text):
    client = OpenAI(api_key=openai_api_key())
    speech_file_path = "output/openai.mp3"
    if os.path.exists(speech_file_path):
        os.remove(speech_file_path)
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=text)

    response.write_to_file(speech_file_path)
    play(speech_file_path)


# say_openai("Emmm...")
