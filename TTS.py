from gtts import gTTS
import os
import pyttsx3
from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES, NAMES


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    random_name = get_random_name(combo=[ADJECTIVES, NAMES], separator="-")
    tts.save(f"{random_name}.mp3")
    os.system("start output.mp3")


if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
