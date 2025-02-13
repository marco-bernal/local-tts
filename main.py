# TODO: ADD comments/document functions, make private functions.
import os
import torch
import pandas as pd
import gradio as gr

from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_audio(model, text):
    tts = TTS(model_name = model).to(device)
    tts.tts_to_file(text = text, file_path="outputs/output.wav")
    return "outputs/output.wav" # Delete

# TODO: Improve UI with gr.Blocks: Phase II.
def launch_interface(models_df):
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
        allow_flagging = "never"
    )

    interface.launch()

def load_models(file_path):
    return pd.read_csv(file_path)

def validate_output_folder(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load models
    models_file_path = 'datasets/english_models.csv'
    english_models = load_models(models_file_path)
    # print('Available models: ', english_models)

    # Create output folder if it doesn't exist
    validate_output_folder('outputs')

    #Launch UI
    launch_interface(english_models)

