"""TTS (text to speech) tool based on coqui-ai/TTS and Gradio.
 https://github.com/coqui-ai/TTS
 https://github.com/gradio-app/gradio
"""
import os
import torch
import pandas as pd
import gradio as gr

from TTS.api import TTS

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

""" 
Generates audio from a gradio input text, based on a selected model.

Args:
    model: gradio dropdown containing available models to TTS. 
    text: user input to be TTS generated.
    
Returns:
    output.wav file inside the 'outputs' folder. 
    Every time a new TTS file is generated it gets replaced.    
"""
def generate_audio(model, text):
    """Generates audio from a gradio input text"""
    tts = TTS(model_name = model).to(DEVICE)
    tts.tts_to_file(text = text, file_path="outputs/output.wav")
    return "outputs/output.wav" # Delete

# TODO: Improve UI with gr.Blocks: Phase II.
def _launch_interface(models_df):
    interface = gr.Interface(
        fn = generate_audio,
        inputs = [
            gr.Dropdown(choices = list(models_df['name']), label="Available english models:"),
            gr.Text(label="Text:")
        ],
        outputs = [
            gr.Audio(label="Audio")
        ],
        title = "Text to Speech PoC with coqui-ai/TTS and Gradio.",
        flagging_mode = "never"
    )

    interface.launch()

def _load_models(file_path):
    return pd.read_csv(file_path)

def _validate_output_folder(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Load available models
    MODELS_FILE_PATH = 'datasets/english_models.csv'
    english_models = _load_models(MODELS_FILE_PATH)
    # print('Available models: ', english_models)

    #Create output folder if it doesn't exist
    _validate_output_folder('outputs')

    #Launch UI
    _launch_interface(english_models)
