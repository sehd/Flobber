import os
from src.speak import play


def get_audio_files():
    audio_files = []
    output_dir = "output"

    if not os.path.exists(output_dir):
        return audio_files

    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.lower().endswith((".mp3", ".wav")):
                audio_files.append(os.path.join(root, file))

    return audio_files


if __name__ == "__main__":
    files = get_audio_files()
    for f, i in enumerate(files):
        print(f"{i} - {f}")

    while True:
        choice = input("Select a file to play by number or insert path: ")
        if choice.isdigit() and int(choice) < len(files):
            selected_file = files[int(choice)]
        else:
            selected_file = choice

        play(selected_file)
