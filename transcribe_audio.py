# Placeholder for transcribe_audio.py
import whisper # type: ignore
import os
import tempfile
import moviepy.editor as mp # type: ignore

model = whisper.load_model("base")

def transcribe_audio(video_path):
    temp_audio = tempfile.mktemp(suffix=".mp3")
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(temp_audio, logger=None)
    result = model.transcribe(temp_audio)
    return result['text']