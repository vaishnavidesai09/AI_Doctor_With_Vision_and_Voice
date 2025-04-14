# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

# Install system dependencies (like portaudio)
RUN apt-get update && apt-get install -y portaudio19-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt and your Gradio app to the container
COPY requirements.txt /app/
COPY gradio_app.py /app/

# Install Python dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for your Gradio app (default is 7860)
EXPOSE 7860

# Run your Gradio app
CMD ["python", "gradio_app.py"]
