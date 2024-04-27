import os
import subprocess
from moviepy.editor import VideoFileClip


def convert_video_to_audio(video):
    filename, ext = os.path.splitext(video)
    try:
        clip = VideoFileClip(video)
        clip.audio.write_audiofile(f"{filename}.mp3")
    except KeyError:
        subprocess.call(["ffmpeg", "-y", "-i", video,
                        f"{filename}.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
