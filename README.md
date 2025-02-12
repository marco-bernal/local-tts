## Local TTS (text to speech) tool.
Generates speech from text with non-robotic voices. 

### Environment
##### Manually create a conda env (Hopefully to be replaced by UV)
* conda create -n tts python=3.9 
* conda activate tts

### Dependencies:
* coqui-ai/TTS
  (pip install TTS)

* Gradio Web UI
  (pip install gradio)

### Run:
* Run manually from the project: ```python main.py```
* Go to http://127.0.0.1:7860/, add text as input and click submit.
* Download the audio file generated from the ```outputs``` folder.

### TODO
#### Backend:
* Configure UV to manage dependencies.  
* Refactor code.
* Add unit/integration tests.
* Add a docker file to containerize the app.
* Test the docker image locally.
* Deploy it to a VPS.

#### Frontend:
* Add combo box to add "Available" english models.
* Add button to download the generated wav file.
* Polish the UI.

### Reference:
https://www.youtube.com/watch?v=EyzRixV8s54

#### Tested models:
* 10,tts_models/en/ek1/tacotron2  -> <b>Doesn't work!</b>
* 11,tts_models/en/ljspeech/tacotron2-DDC -> <b>Works well!</b>
* 12,tts_models/en/ljspeech/tacotron2-DDC_ph
* 13,tts_models/en/ljspeech/glow-tts
* 14,tts_models/en/ljspeech/speedy-speech
* 15,tts_models/en/ljspeech/tacotron2-DCA
* 16,tts_models/en/ljspeech/vits
* 17,tts_models/en/ljspeech/vits--neon
* 18,tts_models/en/ljspeech/fast_pitch
* 19,tts_models/en/ljspeech/overflow
* 20,tts_models/en/ljspeech/neural_hmm
* 21,tts_models/en/vctk/vits
* 22,tts_models/en/vctk/fast_pitch
* 23,tts_models/en/sam/tacotron-DDC
* 24,tts_models/en/blizzard2013/capacitron-t2-c50
* 25,tts_models/en/blizzard2013/capacitron-t2-c150_v2
* 26,tts_models/en/multi-dataset/tortoise-v2
* 27,tts_models/en/jenny/jenny
* 32,tts_models/uk/mai/glow-tts
* 33,tts_models/uk/mai/vits
* v3,vocoder_models/en/ek1/wavegrad
* v4,vocoder_models/en/ljspeech/multiband-melgan
* v5,vocoder_models/en/ljspeech/hifigan_v2
* v6,vocoder_models/en/ljspeech/univnet
* v7,vocoder_models/en/blizzard2013/hifigan_v2
* v8,vocoder_models/en/vctk/hifigan_v2
* v9,vocoder_models/en/sam/hifigan_v2