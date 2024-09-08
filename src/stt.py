from openai import OpenAI
from keys import openai_api_key
import platform

if platform.system() == "Windows":
    import whisper

    model = whisper.load_model("base")

    def transcribe_audio_offline(path):
        print("Transcribing audio...")
        result = model.transcribe(path, language="en")
        print("Transcription:")
        print(result["text"])
        return result["text"]


def transcribe_audio_openai(path):
    client = OpenAI(api_key=openai_api_key())

    with open(path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            file=audio_file, model="whisper-1", response_format="text", language="fa"
        )
        print(transcript)
        return transcript
