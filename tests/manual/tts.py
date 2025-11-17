from tts import say_openai

def test_tts():
    text = input("Insert text to be spoken [Hello, world!]: ") or "Hello, world!"
    print("speaking:", text)
    say_openai(text)