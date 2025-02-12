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