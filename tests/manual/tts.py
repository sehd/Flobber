from src.tts import say_openai

if __name__ == "__main__":
    text = input("Insert text to be spoken [Hello, world!]: ") or "Hello, world!"
    print("speaking:", text)
    say_openai(text)
