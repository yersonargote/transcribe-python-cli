import os
import shutil
from datetime import datetime

import pytube
import typer
import whisper
from rich import print

app = typer.Typer()

CURR_DIR = os.path.dirname(os.path.realpath(__file__))


def get_path() -> str:
    directory = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    path = f"{CURR_DIR}/output/{directory}"
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def download_audio(url: str, path: str) -> None:
    video = pytube.YouTube(url)
    audio = video.streams.get_audio_only()
    audio.download(filename=f"{path}/temp.mp3")


def move(src: str, dest: str) -> None:
    shutil.move(f"{src}", f"{dest}/temp.mp3")


def transcribe(model: str, path: str, mode: str) -> None:
    model = whisper.load_model(model)
    result = model.transcribe(f"{path}/temp.mp3", task=mode)

    with open(f"{path}/temp.txt", "w") as f:
        f.write(result["text"])
    print("Done!")


@app.command()
def whisper_cli(
    url: str = typer.Argument(..., help="Youtube video url or video/audio path"),
    model: str = typer.Argument(default="small", help="Name of the model to use"),
    translate: bool = typer.Option(False, help="Translate the video"),
    youtube: bool = typer.Option(True, help="Use pytuve to download the video"),
):
    """
    Transcribe or translate a Youtube video given an URL.
    """

    if translate:
        mode = "translate"
        print("Translating video...")
    else:
        mode = "transcribe"
        print("Transcribing video...")

    path = get_path()
    if youtube:
        download_audio(url=url, path=path)
    else:
        move(url, path)
    transcribe(model=model, path=path, mode=mode)


if __name__ == "__main__":
    app()
