
import whisper

model = whisper.load_model("base")

def transcribe_audio(path):
    print("Transcribing audio...")
    result = model.transcribe(path)
    print("Transcription:")
    print(result["text"])
    return result["text"]