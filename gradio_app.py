import os 
import gradio as gr
from brain_of_the_doctor import encode_image,analyse_image_with_query
from voice_of_patient import record_audio, transcribe_with_groq
from voice_of_doctor import text_to_speech_with_eleven_labs, text_to_speech_with_gtts


from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_file_path, image_filepath):

                
    speech_to_text_output = transcribe_with_groq(stt_model="whisper-large-v3",
                                            audio_file_path=audio_file_path,
                                            GROQ_API_KEY=os.environ.get('GROQ_API_KEY'))


    # Handle the image input
    if image_filepath:
        doctor_response = analyse_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="llama3-70b-8192")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_eleven_labs(input_text=doctor_response, output_filepath="final.mp3",wav_filepath="doctor_voice.wav") 

    return speech_to_text_output, doctor_response, voice_of_doctor


# Get the port from the environment variable, default to 10000 if not set
port = int(os.getenv("PORT", 10000))           
            
            


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice Response")


    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(server_name="0.0.0.0", server_port=port, debug=True)


#link to visit http://127.0.0.1:7860/
