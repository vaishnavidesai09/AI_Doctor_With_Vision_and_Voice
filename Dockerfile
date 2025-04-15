FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    build-essential \
    gcc \
    python3-dev \
    libsndfile1-dev \
    libportaudio2 \
    libportaudiocpp0 \
    ffmpeg \
    alsa-utils \
    pulseaudio \
    libasound2 \
    libasound2-dev \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy application files
COPY requirements.txt /app/
COPY gradio_app.py /app/
COPY brain_of_the_doctor.py /app/
COPY voice_of_doctor.py /app/
COPY voice_of_patient.py /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 10000

# Set the default command
CMD ["python", "gradio_app.py"]
