1. Download `miniforge`:
	```bash
	curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
	```
1. Install `miniforge`:
	```bash
	bash Miniforge3-$(uname)-$(uname -m).sh
	```
1. Create and enter virtual environment:
	```bash
	mamba env create --file environment.yml && mamba activate transcribe
	```
1. Run script to transcribe by replacing the input audio and output transcript file names:
	```bash
	python run.py <input_audio.wav> <output_transcript.txt>
	```