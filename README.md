# Whisper cli to transcribe Youtube video

[**OpenAI Whisper**](https://github.com/openai/whisper)

[**Typer**](https://typer.tiangolo.com)

[**Pytube**](https://pytube.io/en/latest/)

## Install dependencies

```bash
python3 -m venv venv

source ./venv/bin/activate
```

```bash
pip install -r requirements.txt
```
## Run

```bash
python3 main.py url-youtube-video model-name
```

```bash
# Transcribe
python3 main.py https://www.youtube.com/watch?v=9bZkp7q19f0 small

# Translate
python3 main.py https://www.youtube.com/watch?v=9bZkp7q19f0 small --translate 
```

## Problems and solutions

**Note**: You need to have nvidia cuda work ok.

I have some problems with this.

1. ["Could not load dynamic library 'libcudnn.so.8'" when running tensorflow on ubuntu 20.04]()

- ***Solution***

```bash
sudo apt install nvidia-cudnn
```

## Available models and languages

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed. 


|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |
