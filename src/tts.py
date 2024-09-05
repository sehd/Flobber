import pyttsx3
from pathlib import Path
from openai import OpenAI


def say_offline(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 150)

    engine.say(text)
    engine.runAndWait()


def say_openai(text, api_secret):
    client = OpenAI(api_secret=api_secret)
    speech_file_path = Path(__file__) / f"ttsoutput/openai.mp3"
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=text)

    response.write_to_file(speech_file_path)
