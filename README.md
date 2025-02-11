## Local TTS (text to speech) tool.
Generates speech from text with non-robotic voices. 

### Dependencies:
* coqui-ai/ TTS
* Gradio (UI)

### Run:
* run manually from the project: ```python main.py```
* Go to http://127.0.0.1:7860/, add text as input and click submit.
* Download the audio file generated from the ```output``` folder.

### Source:
https://www.youtube.com/watch?v=EyzRixV8s54

### TODO:
* Improve it by customizing the UI and refactoring the code.
* Configure UV to manage dependencies.  
* Add a docker file to containerize the app.
* Test the docker image locally.
* Deploy it in a VPS.
