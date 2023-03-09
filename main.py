import os
from datetime import datetime

import pytube
import typer
from rich import print

import whisper

app = typer.Typer()

CURR_DIR = os.path.dirname(os.path.realpath(__file__))


@app.command()
def transcribe(
    url: str = typer.Argument(..., help="Youtube video url"),
    model: str = typer.Argument(default="small", help="Name of the model to use"),
):
    """
    Transcribe a Youtube video given an URL.
    Example:
    python main.py youtube_url model_name
    python main.py https://www.youtube.com/watch?v=9bZkp7q19f0 small
    """

    print("Transcribing video...")
    print(f"URL: {url}")
    print(f"Model: {model}")

    directory = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    path = f"{CURR_DIR}/output/{directory}"
    if not os.path.exists(path):
        os.makedirs(path)

    video = pytube.YouTube(url)
    audio = video.streams.get_audio_only()
    audio.download(filename=f"{path}/tmp.mp3")

    model = whisper.load_model(model)
    result = model.transcribe(f"{path}/tmp.mp3")

    with open(f"{path}/result.txt", "w") as f:
        f.write(result["text"])
    print("Done!")


if __name__ == "__main__":
    app()
