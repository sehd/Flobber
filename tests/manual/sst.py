from src.stt import transcribe_audio_openai


def test_stt(command_path):
    print("transcribing audio from:", command_path)
    command = transcribe_audio_openai(command_path)
    print(command)


if __name__ == "__main__":
    command_path = (
        input("Insert path to audio file [output/command.wav]: ")
        or "output/command.wav"
    )
    test_stt(command_path)
