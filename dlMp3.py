import os
from pathlib import Path
from yt_dlp import YoutubeDL
import subprocess

root = Path('./music/').absolute()

music_path = f"{str(root)}"

processes = []

ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'outtmpl': {
        'default': '%(title)s.%(ext)s'
    }
}

paths = {'paths': {'home': music_path}}

with open('links.txt', 'r') as ytb_links, YoutubeDL(ydl_opts) as ydl:
    urls = []
    for youtube_url in ytb_links:
        if (not youtube_url.startswith('http')):
            ydl.download(urls)
            urls = []
            if (youtube_url.startswith('.')):
                paths['paths']['home'] = music_path
            else:
                paths['paths']['home'] = music_path + '/'+youtube_url
            ydl.params = ydl.params | paths
        else:
            urls.append(youtube_url)
    ydl.download(urls)


# for process in processes:
#    process.wait()

videos = []


def get_all_files(dir):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        ext = os.path.splitext(path)[1]
        if os.path.isfile(path) and ext == ".mp4":
            videos.append(path)
        elif os.path.isdir(path):
            get_all_files(path)


get_all_files(root)
