import torch
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"

# TODO: Create dictionary or file to load available english models
# Available english models:
#  10: tts_models/en/ek1/tacotron2
#  11: tts_models/en/ljspeech/tacotron2-DDC
#  12: tts_models/en/ljspeech/tacotron2-DDC_ph
#  13: tts_models/en/ljspeech/glow-tts
#  14: tts_models/en/ljspeech/speedy-speech
#  15: tts_models/en/ljspeech/tacotron2-DCA
#  16: tts_models/en/ljspeech/vits
#  17: tts_models/en/ljspeech/vits--neon
#  18: tts_models/en/ljspeech/fast_pitch [already downloaded]
#  19: tts_models/en/ljspeech/overflow
#  20: tts_models/en/ljspeech/neural_hmm
#  21: tts_models/en/vctk/vits
#  22: tts_models/en/vctk/fast_pitch
#  23: tts_models/en/sam/tacotron-DDC
#  24: tts_models/en/blizzard2013/capacitron-t2-c50
#  25: tts_models/en/blizzard2013/capacitron-t2-c150_v2
#  26: tts_models/en/multi-dataset/tortoise-v2
#  27: tts_models/en/jenny/jenny
#
#  32: tts_models/uk/mai/glow-tts
#  33: tts_models/uk/mai/vits
#
#  3: vocoder_models/en/ek1/wavegrad
#  4: vocoder_models/en/ljspeech/multiband-melgan
#  5: vocoder_models/en/ljspeech/hifigan_v2 [already downloaded]
#  6: vocoder_models/en/ljspeech/univnet
#  7: vocoder_models/en/blizzard2013/hifigan_v2
#  8: vocoder_models/en/vctk/hifigan_v2
#  9: vocoder_models/en/sam/hifigan_v2

# TODO: Validate if the output folder exists, else create it.
def generate_audio(text):
    tts = TTS(model_name='tts_models/en/ljspeech/glow-tts').to(device) # Replace model name from dictionary
    tts.tts_to_file(text=text, file_path="outputs/output.wav") # User should choose the file name
    return "outputs/output.wav" # Delete
# Improve UI
gui = gr.Interface(
    fn=generate_audio,
    inputs=[gr.Text(label="Text"),],
    outputs=[gr.Audio(label="Audio"),]
)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui.launch()
