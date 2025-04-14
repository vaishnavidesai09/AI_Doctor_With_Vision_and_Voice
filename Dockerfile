# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

# Install system dependencies (like portaudio, build tools, and ffmpeg)
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    build-essential \
    gcc \
    python3-dev \
    libsndfile1-dev \
    libportaudio2 \
    libportaudiocpp0 \
    ffmpeg \
    libsndfile1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt and your Gradio app to the container
COPY requirements.txt /app/
COPY gradio_app.py /app/
COPY brain_of_the_doctor.py /app/
COPY voice_of_doctor.py /app/
COPY voice_of_patient.py /app/

# Install Python dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for your Gradio app (default is 7860)
EXPOSE 7860

# Run your Gradio app
CMD ["python", "gradio_app.py"]

# Expose the port for your Gradio app (default is 7860)
EXPOSE 7860

# Run your Gradio app
CMD ["python", "gradio_app.py"]
