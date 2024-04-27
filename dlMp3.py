import os
from pathlib import Path
from audioToVideo import convert_video_to_audio
import subprocess

root = Path('./music/').absolute()

music_path = f"{str(root)}"

processes = []

with open('links.txt', 'r') as ytb_links:
    directory = ''
    for youtube_url in ytb_links:
        if(not youtube_url.startswith('http')):
            directory = '/'+youtube_url
            if(youtube_url.startswith('.')):
                directory = ''
        else:
            p = subprocess.Popen(['yt-dlp', '-f', "best[ext=mp4]", "-o", f"{music_path+directory}/%(title)s.%(ext)s", f"{youtube_url}"])
            processes.append(p)

for process in processes:
    process.wait()

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

for video in videos:
    convert_video_to_audio(str(video))
    os.remove(video)