## TTS (text to speech) tool based on coqui-ai/TTS and Gradio.
Generates speech from text with non-robotic voices. 

### Project Dependencies:
* coqui-ai/TTS
  (pip install TTS)

* Gradio Web UI
  (pip install gradio)

### Transversal Dependencies:
* pylint: code quality
  (pip install pylint)  

### UV Environment
* Install UV in the conda base env (Only once): `pip install uv`


* Create and initialize a new project with UV and a specific python version: 

`uv init --python 3.11 mab-tts` 

This command will create a `pyproject.toml` configuration file that contains project's data and dependencies.

Don't forget to rename the entry python file to `main.py`.

* Install dependencies with UV:

`uv add TTS gradio`

This command will create a `uv.lock` file that contains the dependencies and their versions.

* Locally run the app with UV in port 7860:

`uv run main.py --port 7860`

* List available and installed UV python versions:

`uv python list`

* Update the venv with a different python version:

`uv sync -p 3.11`

* Add new dependencies and update the environment:

Delete the `uv.lock` file , `uv add pylint` and `uv sync`


### Docker commands.

* Build the docker image: 

```docker build . -t local/mab-tts:latest```
  
* Run a container on the port `7860` based on the above image: 

```docker run -dp 7860:7860 <image_id>```

* Check the container logs:

```docker logs -f <container_id> ```

### Usage:
* Go to http://127.0.0.1:7860/, select a model, add text as input and click submit.
* Play generated audio. 
* Save locally the audio file generated with the download button.

#### Tested models:
* 10,tts_models/en/ek1/tacotron2  -> <b>Doesn't work!.  Weights only load failed error.</b>
* 11,tts_models/en/ljspeech/tacotron2-DDC -> <b>Works well!</b>
* 12,tts_models/en/ljspeech/tacotron2-DDC_ph -> <b>Works well!</b>
* 13,tts_models/en/ljspeech/glow-tts -> <b>Works well!</b>
* 14,tts_models/en/ljspeech/speedy-speech -> <b>Works well!</b>
* 15,tts_models/en/ljspeech/tacotron2-DCA  -> <b>Doesn't work!.  Weights only load failed error.</b>
* 16,tts_models/en/ljspeech/vits -> <b>Doesn't work!.  No espeak found.</b>
* 17,tts_models/en/ljspeech/vits--neon -> <b>Doesn't work!.  No espeak found.</b>
* 18,tts_models/en/ljspeech/fast_pitch -> <b>Works well!</b>
* 19,tts_models/en/ljspeech/overflow -> <b>Doesn't work!.  No espeak found.</b>
* 20,tts_models/en/ljspeech/neural_hmm -> <b>Doesn't work!.  No espeak found.</b>
* 21,tts_models/en/vctk/vits -> <b>Doesn't work!.  No espeak found.</b>
* 22,tts_models/en/vctk/fast_pitch -> <b>Doesn't work!. Multi-speaker.</b>
* 23,tts_models/en/sam/tacotron-DDC -> <b>Doesn't work!.  No espeak found.</b>
* 24,tts_models/en/blizzard2013/capacitron-t2-c50 -> <b>Doesn't work!.  No espeak found.</b>
* 25,tts_models/en/blizzard2013/capacitron-t2-c150_v2 -> <b>Doesn't work!.  No espeak found.</b>
* 26,tts_models/en/multi-dataset/tortoise-v2 -> <b>Works well!</b> Rating 4.5/5. 
More realistic, but requires GPU and a beefy machine. Otherwise, takes ages to generate the output.
* 27,tts_models/en/jenny/jenny  -> <b>Works well!</b>
* 32,tts_models/uk/mai/glow-tts -> <b>Doesn't work!.  Characters not found.</b>
* 33,tts_models/uk/mai/vits -> <b>Doesn't work!.  Characters not found.</b>
* v3,vocoder_models/en/ek1/wavegrad -> <b>Doesn't work!. use_phonemes.</b> 
* v4,vocoder_models/en/ljspeech/multiband-melgan -> <b>Doesn't work!. use_phonemes.</b> 
* v5,vocoder_models/en/ljspeech/hifigan_v2 -> <b>Doesn't work!. use_phonemes.</b> 
* v6,vocoder_models/en/ljspeech/univnet -> <b>Doesn't work!. use_phonemes.</b> 
* v7,vocoder_models/en/blizzard2013/hifigan_v2 -> <b>Doesn't work!. use_phonemes.</b> 
* v8,vocoder_models/en/vctk/hifigan_v2 -> <b>Doesn't work!. use_phonemes.</b> 
* v9,vocoder_models/en/sam/hifigan_v2 -> <b>Doesn't work!. use_phonemes.</b> 

#### Errors:
* <b>Weights only load failed:</b>

This file can still be loaded, to do so you have two options, do those steps only if you trust the source of the checkpoint. 

        (1) In PyTorch 2.6, we changed the default value of the `weights_only` argument in `torch.load` from `False` to `True`. Re-running `torch.load` with `weights_only` set to `False` will likely succeed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
        (2) Alternatively, to load with `weights_only=True` please check the recommended steps in the following error message.
        WeightsUnpickler error: Unsupported global: GLOBAL TTS.utils.radam.RAdam was not an allowed global by default. Please use `torch.serialization.add_safe_globals([RAdam])` or the `torch.serialization.safe_globals([RAdam])` context manager to allowlist this global if you trust this class/function.


* <b>No espeak found:</b>

No espeak backend found. Install espeak-ng or espeak to your system.


* <b>Multi-speaker:</b>

ValueError: Model is multi-speaker but no `speaker` is provided.


* <b>Characters not found:</b>

[!] Character 'x' not found in the vocabulary. Discarding it.
As a result, audio is distorted and unintelligible.


* <b>KeyError: 'use_phonemes'</b>

tts = TTS(model_name = model).to(device)
 File "/anaconda3/envs/tts/lib/python3.9/site-packages/TTS/utils/synthesizer.py", line 184, in _load_tts
    if self.tts_config["use_phonemes"] and self.tts_config["phonemizer"] is None:

### TODO
* MVP:
  * Add unit/integration tests. Research how to do that.
  * Deploy to Huggingface.

* Phase II:
  * Fix broken models if possible. 
  * Polish the UI with gr.Blocks. 
  * Deploy to a VPS.
  * Create CI/CD pipeline w/ GitHub actions.