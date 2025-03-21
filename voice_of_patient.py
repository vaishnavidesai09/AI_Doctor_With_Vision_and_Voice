#step 1 : audio recorder setup(ffmeg and portaudio)
import logging
import speech_recognition as sr
from pydub import  AudioSegment
from io import BytesIO
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_file_path='patient_voice_test.mp3'
record_audio(file_path=audio_file_path)

#step 2 : setup speech to text -STT-model for transcriptions 
from groq import Groq
#GROQ_API_KEY = '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'
GROQ_API_KEY = os.environ.get('GROQ_API_KEY ')
stt_model = 'whisper-large-v3'

def transcribe_with_groq(stt_model,audio_file_path,GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file = open(audio_file_path,'rb')
    transcription= client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text