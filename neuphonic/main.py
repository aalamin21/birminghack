import os
from dotenv import load_dotenv
from pyneuphonic import Neuphonic, TTSConfig, save_audio
from pyneuphonic.player import AudioPlayer
import load_text

# Load the API key from the environment
load_dotenv()
client = Neuphonic(api_key=os.environ.get('NEUPHONIC_API_KEY'))

sse = client.tts.SSEClient()

# TTSConfig is a pydantic model so check out the source code for all valid options
tts_config = TTSConfig(
    speed=1.05,
    lang_code='en', # replace the lang_code with the desired language code.
    voice_id='e564ba7e-aa8d-46a2-96a8-8dffedade48f'
)

# Create an audio player with `pyaudio`
with AudioPlayer() as player:
    message = load_text.text()
    response = sse.send(message, tts_config=tts_config)
    player.play(response)

    player.save_audio('output.wav')  # save the audio to a .wav file