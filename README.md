# 🏥 AI-Powered Health Assistant

## 🚀 Overview
This project leverages **Groq AI**, **Speech Recognition**, **Text-to-Speech (TTS)**, and **Image Analysis** to build an AI-driven health assistant. It allows users to:

✅ Analyze facial images for health conditions 🖼️📊  
✅ Record and transcribe patient speech 🎤➡️📝  
✅ Convert text responses to natural speech using TTS 🎙️🔊

---

## 📌 Features

### 🔑 Step 1: Setup Groq API Key

- Ensure you have a `.env` file with your API key.
- The script loads the API key using `dotenv`.

```python
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
```

---

### 🖼️ Step 2: Convert Image into Required Format

- Convert an image into base64 format for processing.

```python
import base64

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
```

---

### 🤖 Step 3: Analyze Image with Multimodal LLM

- Uses **Groq AI** with `llama-3.2-90b-vision-preview` to analyze the image.

```python
from groq import Groq

def analyse_image_with_query(query, model, encoded_image):
    client = Groq()
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]
    chat_completion = client.chat.completions.create(messages=messages, model=model)
    return chat_completion.choices[0].message.content
```

---

### 🎤 Step 4: Record Audio Input

- Uses **SpeechRecognition** to capture and save audio as an MP3 file.

```python
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

def record_audio(file_path, timeout=20):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source, timeout=timeout)
    audio_segment = AudioSegment.from_wav(BytesIO(audio_data.get_wav_data()))
    audio_segment.export(file_path, format="mp3")
```

---

### 🎙️ Step 5: Convert Speech to Text (STT)

- Uses **Groq's Whisper** model to transcribe audio.

```python
def transcribe_with_groq(stt_model, audio_file_path, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(model=stt_model, file=audio_file, language="en")
    return transcription.text
```

---

### 🔊 Step 6: Text-to-Speech (TTS)

#### 🎵 Option 1: GTTS (Google Text-to-Speech)

```python
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    audio_obj = gTTS(text=input_text, lang='en', slow=False)
    audio_obj.save(output_filepath)
```

#### 🎶 Option 2: ElevenLabs AI Voice

```python
import elevenlabs
from elevenlabs.client import ElevenLabs

def text_to_speech_with_eleven_labs(input_text, output_filepath):
    client = ElevenLabs(api_key='YOUR_ELEVENLABS_API_KEY')
    audio = client.generate(text=input_text, voice="Aria", output_format='mp3_22050_32', model='eleven_turbo_v2')
    elevenlabs.save(audio, output_filepath)
```
![image](https://github.com/user-attachments/assets/1146ae46-d5fe-4733-bd2f-f0d8404736fa)

---

## 📦 Installation & Setup

1️⃣ Clone the repository:
```bash
git clone https://github.com/your-username/ai-health-assistant.git
cd ai-health-assistant
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Set up API keys in `.env` file:
```
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

4️⃣ Run the application:
```bash
python main.py
```

---

## 🤝 Contributing
Feel free to submit issues or pull requests to improve this project! 🚀

---

## 📜 License
This project is licensed under the Apache License.

---

## 💡 Future Enhancements
✅ Improve response accuracy with fine-tuned AI models 🤖
✅ Integrate real-time face health diagnosis 🏥
✅ Support additional languages for transcription & TTS 🌍

---

💙 **Made with AI & Passion by Vaishnavi!** 🚀


