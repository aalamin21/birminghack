import os
from dotenv import load_dotenv
from pyneuphonic import Neuphonic, TTSConfig, save_audio
import hashlib


# Load the API key from the environment
load_dotenv()
client = Neuphonic(api_key=os.environ.get('NEUPHONIC_API_KEY'))

sse = client.tts.SSEClient()

# # Create an audio player with `pyaudio`
# def generate_audio(script):
#     script_hash = int(hashlib.sha256(script.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
#     response = sse.send(script, tts_config=tts_config)
#     audio_bytes = bytearray()
#     for item in response:
#         audio_bytes += item.data.audio
#     print(response)
#     file_name = f'{script_hash}.wav'
#     save_audio(audio_bytes=audio_bytes, file_path=os.path.join('app', 'static', 'audio', file_name))  # save the audio to a .wav file
#     return file_name


def generate_audio(script, lang):
    # TTSConfig is a pydantic model so check out the source code for all valid options
    tts_config = TTSConfig(
        speed=1.05,
        lang_code=lang,  #  replace the lang_code with the desired language code.
    )

    script_hash = int(hashlib.sha256(script.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
    response = sse.send(script, tts_config=tts_config)

    audio_bytes = bytearray()

    print("Response received:", response)  # Check what the response object contains

    for item in response:
        if hasattr(item, "data") and hasattr(item.data, "audio"):  # Ensure audio data exists
            print("Chunk received:", len(item.data.audio), "bytes")  # Log chunk sizes
            audio_bytes += item.data.audio
        else:
            print("No audio in this response item:", item)

    if not audio_bytes:
        print("ERROR: No audio bytes received!")

    file_name = f'{script_hash}.wav'
    save_audio(audio_bytes=audio_bytes, file_path=os.path.join('app', 'static', 'audio', file_name))

    return file_name