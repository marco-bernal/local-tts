import torch
from TTS.api import TTS
import gradio as gr
import pandas as pd

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_models(file_path):
    return pd.read_csv(file_path)

# TODO: Validate if the output folder exists, else create it.
def generate_audio(model, text):
    tts = TTS(model_name = model).to(device)
    tts.tts_to_file(text = text, file_path="outputs/output.wav")
    return "outputs/output.wav" # Delete

# TODO: Improve UI
def launch_interface(models_df):
    interface = gr.Interface( #TODO: Add title and bar title
        fn = generate_audio,
        inputs = [
            gr.Dropdown(choices = list(models_df['name']), label="Available english models"),
            gr.Text(label="Text") #TODO: Change size to a taller one
        ],
        outputs = [
            gr.Audio(label="Audio") #TODO: Remove Flag button
        ]
    )

    interface.launch()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load models
    models_file_path = 'datasets/english_models.csv'
    english_models = load_models(models_file_path)
    #TODO: Test all the models and update the README file accordingly. Once finished, remove unusable models from the csv file

    # print('Available models: ', english_models)
    #Launch UI
    launch_interface(english_models)

