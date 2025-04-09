from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os
from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES, NAMES

# Get it from ElevenLabs website

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)


def text_to_speech(text, voice_id="JBFqnCBsd6RMkjVDRZzb", model="eleven_multilingual_v2"):
    output_dir = "TTS_Audio"
    os.makedirs(output_dir, exist_ok=True)

    # Generate audio (returns a generator)
    audio_stream = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id=model,
        output_format="mp3_44100_128",
    )

    # Collect all chunks from the generator
    audio_data = bytes()
    for chunk in audio_stream:
        if chunk:
            audio_data += chunk

    # Generate a random filename
    random_name = get_random_name(combo=[ADJECTIVES, NAMES], separator='_')
    filename = f"{random_name}.mp3"
    full_path = os.path.join(output_dir, filename)

    # Save audio to file
    with open(full_path, "wb") as f:
        f.write(audio_data)

    print(f"Saved as: {filename}")
    return filename


if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    saved_file = text_to_speech(text)
